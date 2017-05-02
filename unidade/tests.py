from django.test import TestCase
from django.test import Client
from .models import Unidade

class UnidadeTestCase(TestCase):
    
    def setUp(self):
        Unidade.objects.create(unidade="Jessé Freire", endereco="SCS")
        Unidade.objects.create(unidade="Taguatinga", endereco="SCS")

    def test_unidade_exists(self):
        beleza = Unidade.objects.get(unidade="Jessé Freire")
        tecnologia = Unidade.objects.get(unidade="Taguatinga")
        self.assertEqual(beleza.unidade, "Jessé Freire")
        self.assertEqual(tecnologia.unidade, "Taguatinga")

    def test_view_home(self):
        client = Client()
        response = client.get('/unidade/')
        self.assertEqual(response.status_code, 200)

    def test_view_detail(self):
        client = Client()
        response = client.get('/unidade/1/')
        self.assertEqual(response.status_code, 200)

    # def text_get_all(self):
    #   eixos = Eixo.objects.all()
    #   self.assertIsInstance(a, b)
