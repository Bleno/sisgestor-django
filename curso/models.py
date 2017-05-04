from django.db import models
from eixo.models import Eixo

class Curso(models.Model):
    """ tb_curso """
    eixo = models.ForeignKey(Eixo)
    curso = models.CharField(max_length=45)
    sigla = models.CharField(max_length=3)
    ativo = models.BooleanField(default=True)
