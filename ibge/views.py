from curses.ascii import isalnum
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
    lista_estados = requisicao_estados.json()
    
    regiao_selecionada = request.GET['regiao']
    if regiao_selecionada.isnumeric() == True:
        regiao_selecionada = request.GET['regiao']
    else:
        regiao_selecionada = str(0)
    
    api_regiao_selecionada = 'https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/' + regiao_selecionada
    requisicao_regiao = requests.get(api_regiao_selecionada)
    dados_regiao = requisicao_regiao.json()
     
    dicionario_estados = {}
    dicionario_regiao_selecionada_projecoes = {}
    
    
    for indice, valor in enumerate(lista_estados):
        dicionario_estados[indice] = valor
    for valor_regiao in dados_regiao:
        dicionario_regiao_selecionada_projecoes[indice] = valor_regiao
        
    
    contexto = {
        "estados": dicionario_estados,
        "regiao_selecionada" : int(regiao_selecionada),
        "dados_projecoes" : dados_regiao,
    }    
    return render(request, "ibge\estados.html", contexto)

def dados_regioes(request):
    pass