from django.db import models


class Escolaridade(models.Model):
    """
    Description: Model Description
    """

    escolaridade = models.CharField(max_length=45)
    

    class Meta:
        pass
