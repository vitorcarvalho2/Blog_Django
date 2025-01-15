from django.views.generic import TemplateView
from .models import Equipe, Servico
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['equipe'] = Equipe.objects.all()
        context['servico'] = Servico.objects.all()
        return context