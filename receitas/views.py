from django.shortcuts import render
from .models import Receita
# from django.http import HttpResponse


def index(request):
    receitas = Receita.objects.all()
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request):
    return render(request, 'receita.html')
    # return HttpResponse('<h1> Receitas </h1> <br> <h2> Bem vindo </h2>')
