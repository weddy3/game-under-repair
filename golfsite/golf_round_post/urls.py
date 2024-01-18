from django.urls import path
from . import views
from .views import RoundListView, RoundDetailView, RoundCreateView, RoundUpdateView, RoundDeleteView

urlpatterns = [
    path("", RoundListView.as_view(), name="golf-round-home"),
    path("about/", views.about, name="golf-about"),
    path("golf-round/<int:pk>/", RoundDetailView.as_view(), name="golf-round-detail"),
    path("round/new/", RoundCreateView.as_view(), name="golf-round-create"),
    path("golf-round/<int:pk>/update/", RoundUpdateView.as_view(), name="golf-round-update"),
    path("golf-round/<int:pk>/delete/", RoundDeleteView.as_view(), name="golf-round-delete")
]
