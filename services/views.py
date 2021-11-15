from django.shortcuts import render, get_object_or_404
from testimonials.models import Testimonial
from core.models import FAQ
from .models import Service


def service_list(request):
    services = Service.objects.all()[:6]
    faq = FAQ.objects.all()[:6]
    context = {
        "services": services,
        "faq": faq
    }
    return render(request, 'services/pages/services.html', context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    testimonials = Testimonial.objects.all()[:9]

    context = {
        'service': service,
        'testimonials': testimonials,
    }
    return render(request, 'services/pages/service.html', context)
