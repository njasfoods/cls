from django.urls import path

from . import views

app_name = "core"


urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]
