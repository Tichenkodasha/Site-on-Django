from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hotel-home'),
    path('about/', views.about, name='hotel-about'),
]