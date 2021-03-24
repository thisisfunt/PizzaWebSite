from django.shortcuts import render
from Bl.productDB import GetAllProducts

def ViewMainPage(request):
    """return main page with all products"""
    q = GetAllProducts()
    return render(request, 'index.html', {'products' : q})

def ViewBacketPage(request):
    """return page with backet"""
    return render(request, 'basket.html')
