from django.shortcuts import render
import requests

def index(request):
    api_regioes = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes"
    requisicao_regioes = requests.get(api_regioes)

    try:
        lista = requisicao_regioes.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario_regioes = {}
    for indice, valor in enumerate(lista):
        dicionario_regioes[indice] = valor
    

    contexto = {
        "regioes": dicionario_regioes
    }

    return render(request, "ibge\index.html", contexto)

def estados(request):
    api_estados = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    requisicao_estados = requests.get(api_estados)

    
    lista = requisicao_estados.json()
    
    dicionario_estados = {}
    for indice, valor in enumerate(lista):
        dicionario_estados[indice] = valor
        
    contexto = {
        "estados": dicionario_estados
    }
    

    return render(request, "ibge\estados.html", contexto)
    