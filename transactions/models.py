from django.db import models

class Transaction(models.Model):
    type = models.CharField(max_length=1)
    date = models.CharField(max_length=8)
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=6)
    owner = models.CharField(max_length=14)
    store = models.CharField(max_length=18)
