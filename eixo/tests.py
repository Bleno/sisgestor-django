from django.test import TestCase
from django.test import Client
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

    def test_view_home(self):
        client = Client()
        response = client.get('/eixo/')
        self.assertEqual(response.status_code, 200)

    def test_view_detail(self):
        client = Client()
        response = client.get('/eixo/1/')
        self.assertEqual(response.status_code, 200)

    # def text_get_all(self):
    #   eixos = Eixo.objects.all()
    #   self.assertIsInstance(a, b)
