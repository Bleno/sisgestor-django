from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Eixo

# Create your views here.
def index(request):
    eixos = Eixo.objects.all()
    context = { 'eixos' : eixos }
    return render(request, 'list.html', context)

def detail(request, eixo_id):
    eixo = get_object_or_404(Eixo, pk=eixo_id)
    return render(request, 'detail.html', {'eixo': eixo})

def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    eixo = Eixo.objects.create(eixo=request.POST['eixo'])
    # eixo.save()
    return HttpResponseRedirect(reverse('eixo'))