from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Unidade
from django.urls import reverse


# Create your views here.
def index(request):
    unidades = Unidade.objects.all()
    return render(request, "list_unidade.html", {"unidades": unidades})

def add(request):
    if request.method == 'GET':
        return render(request, "add_unidade.html")
    unidade = Unidade(unidade=request.POST['unidade'], endereco=request.POST['endereco'])
    unidade.save()
    return HttpResponseRedirect(reverse('unidade'))

def detail(request, unidade_id):
    unidade = get_object_or_404(Unidade, pk=unidade_id)
    context = {'unidade': unidade}
    return render(request, "detail_unidade.html", context)