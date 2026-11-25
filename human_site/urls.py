from django.urls import path
from catalog import views

urlpatterns = [
    path("", views.home, name="home"),
    path("systems/", views.listing, {"kind": "systems"}, name="systems"),
    path("diseases/", views.listing, {"kind": "diseases"}, name="diseases"),
    path("health/", views.health, name="health"),
    path("about/", views.about, name="about"),
    path("<slug:slug>/", views.detail, name="detail"),
]
