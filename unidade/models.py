from django.db import models

# Create your models here.

class Unidade(models.Model):
    """docstring for Unidade"""
    
    unidade = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45)
    ativo = models.BooleanField(default=True)
        