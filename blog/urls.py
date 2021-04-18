from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard', views.dashboard, name='user-dashboard'),
    path('about/', views.about, name='blog-about'),
    path('dashboard/spotify', views.register_spotify, name='spotify'),
    path('dashboard/confirmspotify', views.confirm_spotify, name='confirm-spotify'),
]
