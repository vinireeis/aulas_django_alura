from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    receitas = {
        1: 'Lasanha',
        2: 'Sopa de legumes',
        3: 'Sorvete',
        4: 'Bolo de Cenoura',
    }
    dados = {
        'nome_das_receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request):
    return render(request, 'receita.html')
    # return HttpResponse('<h1> Receitas </h1> <br> <h2> Bem vindo </h2>')
