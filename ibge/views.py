from django.shortcuts import render
import requests

def index(request):
    api_regioes = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes"
    requisicao_regioes = requests.get(api_regioes)

    try:
        lista = requisicao_regioes.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "regioes": dicionario
    }

    return render(request, "ibge\index.html", contexto)

def estados(request):
    api_estados = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    
    try:
        pass
    except ValueError:
        pass
    