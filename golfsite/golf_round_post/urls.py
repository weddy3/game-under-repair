from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='golf-round-home'),
    path('about/', views.about, name='golf-about')
]
