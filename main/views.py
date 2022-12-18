from django.shortcuts import render, redirect
from main.models import aboutAdmin, adminService
from main.forms import newUserForm


def render_index_page(request):
    return render(request, 'main/index.html')


def render_about_page(request):
    aAdmin = aboutAdmin.objects.all()[0]
    about_data = {
        'name': aAdmin.name,
        'desc': aAdmin.description,
        'bday': aAdmin.birthday,
        'website': aAdmin.website,
        'phone': aAdmin.phone,
        'city': aAdmin.city,
        'age': aAdmin.age,
        'degree': aAdmin.degree,
        'email': aAdmin.email,
        'freelance': aAdmin.freelance,
        'interest_list': [i.strip() for i in aAdmin.interestes.split(',') if i != ''],
    }
    return render(request, 'main/about.html', {'about_data': about_data})


def render_contact_page(request):
    return render(request, 'main/contact.html')


def render_services_page(request):
    obj = adminService.objects.all()[0]
    data = {
        'serviceListMajor': [i.strip() for i in obj.serviceNameMajor.split(',') if i != ''],
        'serviceListMinor': [i.strip() for i in obj.serviceNameMinor.split(',') if i != ''],
    }
    return render(request, 'main/services.html', {'serviceData': data})


def render_allprojects_page(request):
    return render(request, 'main/allprojects.html')


def render_applist_page(request):
    return render(request, 'main/applist.html')


def registration(request):
    if request.method == 'POST':
        form = newUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('')
    form = newUserForm()
    return render(request, 'main/registration.html', {'form': form})


def login(request):
    pass
