from django.shortcuts import render, get_object_or_404

from core.utils import get_full_context, get_page_seo
from testimonials.models import Testimonial
from core.models import FAQ, Page
from .models import Service


def service_list(request):
    services = Service.objects.all()[:6]
    faq = FAQ.objects.filter(service__isnull=True)[:6]
    page = get_page_seo(slug='services')
    context = {
        'page': page,
        "services": services,
        "faq": faq
    }
    context = get_full_context(context)
    return render(request, 'services/pages/services.html', context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    testimonials = Testimonial.objects.all()[:9]
    gallery_images = service.galleryimage_set.all().select_related('image')
    gallery_videos = service.galleryvideo_set.all()
    faq = service.faq_set.all()
    context = {
        'service': service,
        'testimonials': testimonials,
        'gallery_images': gallery_images,
        'gallery_videos': gallery_videos,
        'faq': faq
    }
    context = get_full_context(context)
    return render(request, 'services/pages/service.html', context)
