from django.urls import path, include
from .views import HomeView, about
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
]