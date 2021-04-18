from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard', views.dashboard, name='user-dashboard'),
    path('about/', views.about, name='blog-about'),
    path('sleepy-driver/', views.driver_is_sleepy, name='sleepy-driver')
]
