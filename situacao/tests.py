from django.test import TestCase
from django.test import Client
from .models import Situacao

class SituacaoTestCase(TestCase):
    
    def setUp(self):
        Situacao.objects.create(situacao="aposentado")
        Situacao.objects.create(situacao="Férias")

    def test_situacao_exists(self):
        aposentado = Situacao.objects.get(situacao="aposentado")
        ferias = Situacao.objects.get(situacao="Férias")
        self.assertEqual(aposentado.situacao, "aposentado")
        self.assertEqual(ferias.situacao, "Férias")

    def test_view_home(self):
        client = Client()
        response = client.get('/situacao/')
        self.assertEqual(response.status_code, 200)

    def test_view_detail(self):
        client = Client()
        response = client.get('/situacao/1/')
        self.assertEqual(response.status_code, 200)

    # def text_get_all(self):
    #   situacaos = situacao.objects.all()
    #   self.assertIsInstance(a, b)
