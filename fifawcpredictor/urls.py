from django.urls import path
from . import views


urlpatterns = [
    path('', views.fifawcpredictorhome, name='fifa_home_page_url'),
    path('test/', views.test, name='test'),

]
