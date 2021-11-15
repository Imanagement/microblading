from django.shortcuts import render
from services.models import Service
from .forms import ContactUsForm
from django.http import JsonResponse

from .models import ContactUsModel


def index(request):
    services = Service.objects.all()[:3]
    context = {
        'services': services
    }
    return render(request, 'core/pages/home.html', {})


def contact_us_view(request):
    if request.method == "POST":
        return JsonResponse({"message": "Please provide all required data"}, status=500)
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
        "form": form
    }
    return render(request, 'core/pages/contact-us.html', context)