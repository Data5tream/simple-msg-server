from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView

from simple_msg_server.models import MsgForm, MsgEntry


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'simple_msg_server/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = MsgForm.objects.all()
        context['entries'] = MsgEntry.objects.all().order_by('-created')[:10]
        return context


@method_decorator(login_required, name='dispatch')
class FormDetailView(DetailView):
    model = MsgForm
    context_object_name = 'form'


@method_decorator(login_required, name='dispatch')
class FormEntryDetailView(DetailView):
    model = MsgEntry
    context_object_name = 'entry'
