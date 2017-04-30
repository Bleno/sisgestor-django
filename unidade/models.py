from django.db import models

# Create your models here.

class Unidade(models.Model):
    """docstring for Unidade"""
    id = models.IntegerField(primary_key=True)
    unidade = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45)
    ativo = models.BooleanField(default=True)
        