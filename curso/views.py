from django.shortcuts import render
from .models import Curso

# Create your views here.
def curso(request):
	cursos = Curso.objects.all()
	context = { 'cursos': cursos }
	return render(request, 'curso.html', context)