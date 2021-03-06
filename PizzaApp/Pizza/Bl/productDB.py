from MainApp.models import product as productDB
from loguru import logger

logger.add("../../main.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB")

def GetAllProducts():
    """return all info about all pizza"""
    q = productDB.objects.all()
    return q

def GetProductsFromBasket(cookie : str):
    productList = []
    for productId in cookie.split("s"):
        productList.append(productDB.objects.filter(id=productId)[0])
    return productList