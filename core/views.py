from django.core.cache import cache, caches
from django.core.cache.utils import make_template_fragment_key
from django.http import JsonResponse
from django.shortcuts import render
from blog.models import Post
from portfolio.models import PortfolioItem
from services.models import Service
from .forms import ContactUsForm
from .models import ContactUsModel, Page
from .utils import get_full_context, get_page_seo


def index(request):
    services = Service.objects.all()[:3]
    page = get_page_seo(main_page=True)
    context = {
        'page': page,
        'services': services,
        'popular_services': services
    }
    context = get_full_context(context)
    return render(request, 'core/pages/home.html', context)


def contact_us_view(request):
    if request.method == "POST":
        # return JsonResponse({"message": "Please provide all required data"}, status=500)
        try:
            form = ContactUsForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                message = form.cleaned_data['message']
                contact_us_model = ContactUsModel.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    message=message
                )
                contact_us_model.save()
            else:
                return JsonResponse({"message": "Please provide all required data"}, status=200)
            return JsonResponse({"message": "Our specialists will contact you as soon as possible"})
        except Exception:
            return JsonResponse({"message": "Something went wrong, please contact our specialists"})
    else:
        form = ContactUsForm()
    context = {
        "page": get_page_seo(slug='contact-us'),
        "form": form
    }
    context = get_full_context(context)
    return render(request, 'core/pages/contact-us.html', context)


def about_us_view(request):
    context = {
        'page': get_page_seo(slug='about-us')
    }
    context = get_full_context(context)
    return render(request, 'core/pages/about-us.html', context)


def search_view(request):
    pass
