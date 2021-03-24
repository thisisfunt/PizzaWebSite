from django.db import models

class product(models.Model):
    """table with products"""
    name = models.CharField(max_length=25)              #name of product (Четыри сыра, Кола)
    imageRef = models.CharField(max_length=255)         #ref for image of product(http://mysite/img/pizza.jpg)
    discription = models.TextField()                    #discription of product (сыр сосиски майонез тесто)
    price = models.IntegerField()                       #price of product in rubles (299)

    def __str__(self):
        return self.name
