from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="wire24"),

    path("contactUs/", views.contactUs, name="contactUs"),
    path("aboutUs/", views.aboutUs, name="aboutUs"),
    path("termsofservices/", views.termsOfServices, name="termsofservices")
]
