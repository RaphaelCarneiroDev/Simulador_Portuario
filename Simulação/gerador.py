#
# MODULO gerador.py CRIA METODOS PARA GERAR CONTAINERS, DOCAS E NAVIOS ALEATORIAMENTE
# ALÉM DE GERAR O PORTO COM OS VALORES SELECIONADOS
#


import sys
import os
import random

sys.path.append(                                                ## ultiliza o 'sys' e o 'os' para que o arquivo coloque como raiz                                                            
    os.path.abspath(                                            ## do projeto inteiro ( para conseguir ler os import)
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from entidades.cContainer import cContainer
from entidades.cNavio import cNavio
from entidades.cDoca import cDoca
from entidades.cPorto import cPorto

# *******************************************************

## Cria listas de empresas, tipos e destinos para gerar containers e navios aleatoriamente

empresas = [
    "Maersk",
    "MSC",
    "TransBahia",
    "OceanCargo",
    "GlobalShip"
]

tipos = [
    "Alimento",
    "Eletronico",
    "Medicamento",
    "Roupa",
    "Industrial"
]

destinos = [
    "Salvador",
    "Santos",
    "Rio de Janeiro",
    "Recife",
    "Fortaleza",
    "Lauro de Freitas"
]

# *******************************************************

def gerarContainer(prioridade = None): ## Função para gerar container pegando sua prioridade como parametro ( se nao for passado, pega None como default)

    if prioridade == None:                  ## Se a prioridade for None, gera uma prioridade aleatoria de 1 a 4
        prioridade = random.randint(1, 4)

    ID = random.randint(10000, 99999)      ## Gera o ID do container aleatorio entre 10000 e 99999

    peso = random.randint(10, 40)           ## Gera o peso do container aleatorio entre 10 e 40 ( Toneladas )

    destino = random.choice(destinos)       ## Gera o destino do container aleatorio entre os destinos da lista 

    empresa = random.choice(empresas)       ## Gera a empresa do container aleatoria entre as empresas da lista

    tipo = random.choice(tipos)             ## Gera o tipo do container aleatorio entre os tipos da lista

    limitePilha = random.randint(6, 9)      ## Gera o limite de empilhamento ( no solo ) entre 6 e 9

    container = cContainer(     ## Cria o container e usa todos os valores gerados como parametro
        ID,
        peso,
        destino,
        prioridade,
        empresa,
        tipo,
        limitePilha
    )

    return container


# *******************************************************

def gerarNavio():                                   ## Metodo para gerar o Navio Aleatorio

    nome = f"NAVIO-{random.randint(100,999)}"       ## Gera um Nome para o Navio sendo NAVIO-"Algum numero entre 100 e 999"

    empresa = random.choice(empresas)               ## Gera a empresa do Navio aleatoria entre as empresas a lista

    prioridade = random.randint(1, 4)               ## Gera uma prioridade aleatoria entre 1 - 4

    qtdPilhas = random.randint(2, 5)                ## Gera uma quantidade de pilhas que o Navio pode carregar, entre 2, 5

    alturaMax = random.randint(4, 5)                 ## Gera uma altura maxima de containers aleatorio entre 4 - 5

    navio = cNavio(
        nome,   
        empresa,
        prioridade,
        qtdPilhas,
        alturaMax
    )

    return navio
# *******************************************************

def popularNavio(navio):                                # Metodo para encher o Navio de container

    capacidade = navio.getCapacidadeTotal()             # pega a capacidade e a prioridade do navio

    prioridade = navio.getPrioridade()

    for i in range(capacidade):                         # Enquanto o navio nao encher, gera container e embarca

        container = gerarContainer(prioridade)

        navio.embarcar(container)

    return navio

# *******************************************************

def gerarDoca():                                        # Função para gerar uma doca ( CADA DOCA TEM SEU PATIO ), e seu respectivo patio

    nome = f"DOCA-{random.randint(1,99)}"   # Nome aleatorio

    qtdPilhasPatio = random.randint(30, 60)  # quantidade de pilhas no patio aleatoria

    alturaPatio = random.randint(6, 9)      # altura de pilha aleatoria

    doca = cDoca(
        nome,
        qtdPilhasPatio,
        alturaPatio
    )

    return doca

# *******************************************************

def popularPatio(doca, quantidade):         ## função para adicionar containers no patio

    patio = doca.getPatio()

    armazenados = 0                         ## conta quantos containers foram armazenados

    while armazenados < quantidade and patio.verifica_espaco():     ## Adiciona container ate encher ou acabar a quantidade

        container = gerarContainer()

        if patio.armazenar(container):
            armazenados += 1

    return armazenados

# *******************************************************

def gerarPorto(qtdDocas, qtdNavios):  # Função para gerar o Porto

    porto = cPorto()

    for i in range(qtdDocas):       # Gera as Docas

        doca = gerarDoca()

        popularPatio(
            doca,
            random.randint(130, 200)
        )

        porto.cadastrarDoca(doca)

    for i in range(qtdNavios):      # Gera os Navios

        navio = gerarNavio()

        popularNavio(navio)

        porto.cadastrarNavio(navio)

    return porto
    