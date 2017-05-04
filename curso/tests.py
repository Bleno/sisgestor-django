from django.test import TestCase
from django.test import Client
from .models import Curso
from eixo.models import Eixo

class CursoTestCase(TestCase):
    
    def setUp(self):
        eixo = Eixo.objects.create(eixo="Beleza")
        Curso.objects.create(curso="Cabelereiro", eixo=eixo)
        Curso.objects.create(curso="Técnico em informática", eixo=eixo)

    def test_curso_exists(self):
        beleza = Curso.objects.get(curso="Cabelereiro")
        tecnologia = Curso.objects.get(curso="Técnico em informática")
        self.assertEqual(beleza.curso, "Cabelereiro")
        self.assertEqual(tecnologia.curso, "Técnico em informática")

    def test_view_home(self):
        client = Client()
        response = client.get('/curso/')
        self.assertEqual(response.status_code, 200)

    def test_view_detail(self):
        client = Client()
        response = client.get('/curso/1/')
        self.assertEqual(response.status_code, 200)

    # def text_get_all(self):
    #   eixos = Eixo.objects.all()
    #   self.assertIsInstance(a, b)
