from django.shortcuts import render
from Bl.productDB import GetAllProducts, GetProductsFromBasket
from Bl.OrderRegistration import ReturnPizzaInBasket
from loguru import logger

logger.add("../../main.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB")

@logger.catch
def ViewMainPage(request):
    """return main page with all products"""
    q = GetAllProducts()
    return render(request, 'index.html', {'products' : q})

@logger.catch
def ViewBacketPage(request):
    """return page with backet"""
    q = ReturnPizzaInBasket(request)
    if not(q is False):
        return render(request, 'basket.html', {'productList':q})
    return render(request, 'EmptyBasket.html')