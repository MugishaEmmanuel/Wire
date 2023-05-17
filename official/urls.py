from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="wire24"),
    path("faq/", views.faq, name="faq"),
    path("termsandconditions/", views.terms, name="terms"),
   
]
