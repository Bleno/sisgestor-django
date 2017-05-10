from django.test import TestCase
from django.test import Client
from .models import Escolaridade


class EscolaridadeTestCase(TestCase):
    
    def setUp(self):
        Escolaridade.objects.create(escolaridade="Médio")
        Escolaridade.objects.create(escolaridade="Fundamental")

    def test_escolaridade_exists(self):
        beleza = Escolaridade.objects.get(escolaridade="Médio")
        tecnologia = Escolaridade.objects.get(escolaridade="Fundamental")
        self.assertEqual(beleza.escolaridade, "Médio")
        self.assertEqual(tecnologia.escolaridade, "Fundamental")

    def test_view_home(self):
        client = Client()
        response = client.get('/escolaridade/')
        self.assertEqual(response.status_code, 200)

    def test_view_detail(self):
        client = Client()
        response = client.get('/escolaridade/1/')
        self.assertEqual(response.status_code, 200)

    # def text_get_all(self):
    #   eixos = Eixo.objects.all()
    #   self.assertIsInstance(a, b)
