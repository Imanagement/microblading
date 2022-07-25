import logging

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from testimonials.models import Testimonial
from core.models import FAQ
from .models import Service


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
    print('wel...')
    print(request)
    try:
        service = get_object_or_404(Service, slug=slug)
    except Http404:
        return redirect('/')
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
