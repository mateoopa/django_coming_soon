from django.views.generic import TemplateView
from .models import Content


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['content'] = Content.objects.get(section__name='Home')
        return context
