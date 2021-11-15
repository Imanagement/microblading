from django.shortcuts import render
from django.views.generic import ListView
from .models import PortfolioItem


class PortfolioListView(ListView):
    model = PortfolioItem
    paginate_by = 20
    template_name = 'portfolio/pages/portfolio.html'

    def get_context_data(self, *args, **kwargs):
        super().get_context_data(*args, **kwargs)
        print('a?')