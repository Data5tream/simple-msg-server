from django.views.generic import TemplateView

from simple_msg_server.models import MsgForm, MsgEntry


# Create your views here.
class DashboardView(TemplateView):
    template_name = 'simple_msg_server/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = MsgForm.objects.all()
        context['msgs'] = MsgEntry.objects.all()[:10]
        return context
