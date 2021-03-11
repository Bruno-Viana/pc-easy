from django.db import models
import threading, time
import json
# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    price_boleto = models.FloatField()
    realprice = models.FloatField()
    img_url = models.URLField()
    prod_url = models.URLField()
    def __str__(self):
        return self.nome






