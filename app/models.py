from django.db import models


# Create your models here.
class Clientes(models.Model):
    nomeCliente = models.CharField(max_length=30)
    telefonteCliente = models.CharField(max_length=30)
    enderecoCliente = models.CharField(max_length=80)
    eletrodomestico = models.CharField(max_length=30)
