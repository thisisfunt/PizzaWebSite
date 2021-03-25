from django.shortcuts import render
from Bl.productDB import GetAllProducts, GetProductsFromBasket
from Bl.OrderRegistration import ReturnPizzaInBasket

def ViewMainPage(request):
    """return main page with all products"""
    q = GetAllProducts()
    return render(request, 'index.html', {'products' : q})

def ViewBacketPage(request):
    """return page with backet"""
    q = ReturnPizzaInBasket(request)
    if not(q is False):
        return render(request, 'basket.html', {'productList':q})
    return render(request, 'EmptyBasket.html')