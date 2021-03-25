from django.db import models

class order(models.Model):
    listProducts = models.CharField(max_length=250)         #список продуктов для доставки (по id через пробелы)
    city = models.CharField(max_length=50)                  #город
    street = models.CharField(max_length=50)                #улица
    house = models.CharField(max_length=50)                 #дом
    intercom = models.CharField(max_length=50)              #домофон
    status = models.CharField(max_length=20)

class product_in_order(models.Model):
    idOrder = models.IntegerField()                         #id заказа
    idProduct = models.IntegerField()                       #id продукта