from django.db import models
from eixo.models import Eixo

class Curso(models.Model):
    id = models.IntegerField(primary_key=True)
    id_eixo = models.ForeignKey(Eixo)
    curso = models.CharField(max_length=45)
    sigla = models.CharField(max_length=3)
    ativo = models.BooleanField(default=True)
