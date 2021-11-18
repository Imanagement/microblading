from django.shortcuts import render
from django.views.generic import ListView
from core.utils import get_full_context, get_page_seo
from .models import PortfolioItem


class PortfolioListView(ListView):
    model = PortfolioItem
    paginate_by = 20
    template_name = 'portfolio/pages/portfolio.html'
    context_object_name = 'portfolio_items'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = get_page_seo(slug='gallery')
        context = get_full_context(context)
        return context
