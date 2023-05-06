from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "official/home.html")

def faq(request):
    return render(request, "official/faq.html")

def terms(request):
    return render(request,"official/terms.html")

def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)

def handler500(request):
    return render(request, 'errors/500.html', status=500)