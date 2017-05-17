from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Situacao


def situacao(request):
    situacoes = Situacao.objects.all()
    context = { 'situacoes': situacoes }
    return render(request, "situacao.html", context)

def add(request):
    if request.method == 'POST':
        situacao = Situacao(situacao=request.POST['situacao'])
        situacao.save()
        return HttpResponseRedirect(reverse('situacao'))
    return render(request, "situacao.add.html")

def detail(request, id):
    situacao = get_object_or_404(Situacao, pk=id)
    return render(request, "situacao.detail.html", { 'situacao':  situacao})