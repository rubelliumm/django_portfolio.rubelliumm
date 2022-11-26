from django.urls import path
from . import views
urlpatterns = [
    path('', views.render_index_page, name='index_page_url'),
    path('about/', views.render_about_page, name='about_page_url'),
    path('contact/', views.render_contact_page, name='contact_page_url'),
    path('services/', views.render_services_page, name='service_page_url')
]
