from django.db import models

class Admin(models.Model):
    id = models.CharField(max_length=100)
    name = models.CharField()


class ProductManager(models.Model):
    
    Productprice = models.CharField(max_length=100)
    productimage = models.CharField()
    Productmodel = models.CharField()
    productRam = models.CharField()