from django.db import models

# Create your models here.
#
class Eixo(models.Model):

    id = models.IntegerField(primary_key=True)
    eixo = models.CharField(max_length=45)


