from django.shortcuts import render
from django.http import HttpResponse
from .models import Escolaridade

# Create your views here.

def escolaridade(request):
	escolaridades = Escolaridade.objects.all()
	context = { 'escolaridades': escolaridades }
	return render(request, "escolaridade.html", context)

def detail(request, id):
	return HttpResponse("OK")


def  add(request):
	return HttpResponse("OK")