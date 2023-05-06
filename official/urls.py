from django.urls import path
from . import views

handler404 = 'official.views.handler404'
handler500 = 'official.views.handler500'

urlpatterns = [
    path("", views.home, name="wire24"),
    path("faq/", views.faq, name="faq"),
    path("termsandconditions/", views.terms, name="terms"),
   
]
