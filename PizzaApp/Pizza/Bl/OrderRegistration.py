from MainApp.models import product as productDB
from collections import namedtuple
from loguru import logger

def CheckTheAvailabilityOfProducts(request):
    """check the availability of products in the shopping cart"""
    for cookie in request.COOKIES:
        if 'product' in cookie:
            if request.COOKIES[cookie]:
                return True
    return False

def ReturnPizzaInBasket(request):
    """return all data from basket"""
    if CheckTheAvailabilityOfProducts(request):
        product = namedtuple('product', 'info count')
        productList = []
        for cookie in request.COOKIES:
            if 'product' in cookie:
                productID = int(cookie.replace('product', ''))
                productCOUNT = int(request.COOKIES[cookie])
                productINFO = productDB.objects.filter(id=productID)[0]
                productList.append(product(productINFO, productCOUNT))
        return productList
    return False