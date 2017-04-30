from django.test import TestCase
from .models import Eixo

class EixoTestCase(TestCase):
    
    def setUp(self):
        Eixo.objects.create(eixo="Beleza")
        Eixo.objects.create(eixo="Tecnologia")

    def test_eixo_exists(self):
        beleza = Eixo.objects.get(eixo="Beleza")
        tecnologia = Eixo.objects.get(eixo="Tecnologia")
        self.assertEqual(beleza.eixo, "Beleza")
        self.assertEqual(tecnologia.eixo, "Tecnologia")


    # def text_get_all(self):
    #   eixos = Eixo.objects.all()
    #   self.assertIsInstance(a, b)
