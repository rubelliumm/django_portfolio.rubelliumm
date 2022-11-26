from django.shortcuts import render

# Create your views here.


def render_index_page(request):
    return render(request, 'main/index.html')


def render_about_page(request):
    return render(request, 'main/about.html')


def render_contact_page(request):
    return render(request, 'main/contact.html')


def render_services_page(request):
    return render(request, 'main/services.html')
