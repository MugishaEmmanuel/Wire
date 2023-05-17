from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "official/home.html")

def faq(request):
    return render(request, "official/faq.html")

def terms(request):
    return render(request,"official/terms.html")

