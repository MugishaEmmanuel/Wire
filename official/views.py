from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "official/home.html")

def contactUs(request):
    return render(request, "official/contactUs.html")

def aboutUs(request):
    return render(request, "official/aboutUs.html")

def termsOfServices(request):
    return render(request, "official/terms.html")


def error_404(request, exception):
    return render(request, '404.html')

