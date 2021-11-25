from django.db import models


# Create your models here.
class Clientes(models.Model):
    nomeCliente = models.CharField(max_length=30, default='')
    telefoneCliente = models.CharField(max_length=30, default='')
    enderecoCliente = models.CharField(max_length=80, default='')
    eletrodomestico = models.CharField(max_length=30, default='')
    marcaAparelho = models.CharField(max_length=50, default='')
    valorServico = models.FloatField(default='0')
    Entrega = models.CharField(max_length=80, default='')
    formaPagamento = models.CharField(max_length=50, default='')