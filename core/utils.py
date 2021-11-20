from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db.models import QuerySet

from blog.models import Post
from core.models import Page
from portfolio.models import PortfolioItem
from services.models import Service
from testimonials.models import Testimonial


def get_full_context(context=None) -> dict:
    context = context if context else {}
    context = get_menu_context(context)
    context = get_testimonial_context(context)
    return context


def get_menu_context(context=None) -> dict:
    context = context if context else {}
    key = make_template_fragment_key('aside_header')
    in_cash = cache.get(key)
    if not in_cash:
        menu_context = {
            "menu_services": Service.objects.all()[:10],
            "menu_blog": Post.objects.all()[:10],
        }
        context.update(menu_context)
    return context


def get_testimonial_context(context=None) -> dict:
    context = context if context else {}
    key = make_template_fragment_key('testimonials')
    in_cash = cache.get(key)
    if not in_cash:
        menu_context = {
            'testimonials': Testimonial.objects.all()
        }
        context.update(menu_context)
    return context


def get_page_seo(main_page: bool = False, slug: str = "") -> Page | None:
    page: QuerySet = Page.objects.filter(page_slug=slug) if not main_page else Page.objects.filter(main_page=True)
    return page[0] if len(page) > 0 else None

