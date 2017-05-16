from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Escolaridade
from django.urls import reverse

# Create your views here.

def escolaridade(request):
	escolaridades = Escolaridade.objects.all()
	context = { 'escolaridades': escolaridades }
	return render(request, "escolaridade.html", context)

def detail(request, id):
	escolaridade = get_object_or_404(Escolaridade, pk=id)
	context = {'escolaridade': escolaridade}
	return render(request, "escolaridade.detail.html", context)


def  add(request):
	if request.method == 'POST':
		escolaridade = Escolaridade(escolaridade=request.POST['escolaridade'])
		escolaridade.save()
		return HttpResponseRedirect(reverse('escolaridade'))
	return render(request, "escolaridade.add.html")