from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Curso
from eixo.models import Eixo

# Create your views here.
def curso(request):
    cursos = Curso.objects.all()
    context = { 'cursos': cursos }
    return render(request, 'curso.html', context)

def detail(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    return render(request, 'detail_curso.html', {'curso': curso})

def add(request):
    if request.method == 'GET':
        eixos = Eixo.objects.all()
        return render(request, 'add_curso.html', {'eixos': eixos})
    curso = Curso(curso=request.POST['curso'],
                  sigla=request.POST['sigla'],
                  eixo=Eixo.objects.get(pk=request.POST['eixo'])
                  )
    curso.save()
    return HttpResponseRedirect(reverse('curso'))

