from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def main(request: HttpRequest):
    return render(request, 'mainapp/index.html')

def products(request: HttpRequest):
    return render(request, 'mainapp/products.html')

def contact(request: HttpRequest):
    return render(request, 'mainapp/contact.html')