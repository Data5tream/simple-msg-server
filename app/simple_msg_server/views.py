import json
import re
import uuid
from http import HTTPStatus

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView, ListView, CreateView

from .models import MsgForm, MsgEntry


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'simple_msg_server/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = MsgForm.objects.all()
        context['entries'] = MsgEntry.objects.all().order_by('-created')[:10]
        return context


class FormListView(LoginRequiredMixin, ListView):
    model = MsgForm
    context_object_name = 'forms'


class FormDetailView(LoginRequiredMixin, DetailView):
    model = MsgForm
    context_object_name = 'form'


class FormAddView(LoginRequiredMixin, CreateView):
    model = MsgForm
    template_name = 'simple_msg_server/msgform_add.html'
    fields = ['name', 'desc', 'fields']
    success_url = '/forms'

    def form_valid(self, form):
        form.instance.endpoint = uuid.uuid4()
        return super().form_valid(form)


class FormEntryDetailView(LoginRequiredMixin, DetailView):
    model = MsgEntry
    context_object_name = 'entry'


@method_decorator(csrf_exempt, name='dispatch')
class CollectFormEntryView(View):
    """create new entries via the API"""

    def post(self, request, endpoint):
        # make sure that we got a valid UUID
        form = MsgForm.objects.filter(endpoint=endpoint).first()
        if not form:
            return JsonResponse({}, status=HTTPStatus.NOT_FOUND)

        # decode JSON data or get form data
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        elif request.content_type == 'multipart/form-data':
            data = request.POST
        else:
            return JsonResponse({'error': 'invalid_content_type'}, status=HTTPStatus.BAD_REQUEST)

        # validate input
        cleaned_data = {}
        errors = {}

        # check email for validity
        email_re = re.compile('\S+@\S+\.\S+')

        # validate fields
        for field in form.fields:
            if field in data:
                if isinstance(data[field], str) and (form.fields[field] == 'string' or
                                                     form.fields[field] == 'email' and email_re.match(data[field])):
                    cleaned_data[field] = data[field]
                else:
                    errors[field] = 'invalid_type'
            else:
                errors[field] = 'missing_field'

        # if there are errors, return the error message, otherwise create the entry
        if errors:
            return JsonResponse(errors, status=HTTPStatus.BAD_REQUEST)

        entry = MsgEntry()
        entry.form = form
        entry.content = cleaned_data
        entry.save()

        return JsonResponse(cleaned_data, status=HTTPStatus.CREATED)
