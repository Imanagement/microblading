import logging

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils.translation import get_language

from testimonials.models import Testimonial
from core.models import FAQ
from .models import Service
from core.services.redirects import get_path_to_home_page


logger = logging.getLogger(__name__)


def service_list(request):
    services = Service.objects.all()
    faq = FAQ.objects.filter(service__isnull=True)[:6]
    context = {
        "services": services,
        "faq": faq
    }
    return render(request, 'services/pages/services.html', context)


def service_detail(request, slug):
    try:
        current_language = get_language()
        if current_language == 'en':
            service_qs = Service.objects.filter(slug_en=slug)
            if not service_qs:
                service_qs = Service.objects.filter(slug_es=slug)
                return redirect('/services/' + service_qs[0].slug_en)
        else:
            service_qs = Service.objects.filter(slug_es=slug)
            if not service_qs:
                service_qs = Service.objects.filter(slug_en=slug)
                return redirect('/es/services-es/' + service_qs[0].slug_es)
        service = service_qs[0]
        extra_prices = service.extraprice_set.all()
        testimonials = Testimonial.objects.all()[:9]
        gallery_images = service.galleryimage_set.all().select_related('image')
        gallery_videos = service.galleryvideo_set.all()
        faq = service.faq_set.all()
        context = {
            'service': service,
            'testimonials': testimonials,
            'gallery_images': gallery_images,
            'gallery_videos': gallery_videos,
            'faq': faq,
            'extra_prices': extra_prices,
        }
        return render(request, 'services/pages/service.html', context)
    except Exception:
        return redirect(get_path_to_home_page())
