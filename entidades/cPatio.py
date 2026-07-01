#
# CLASSE cPatio
#

from TAD.cPilha import cPilha
from TAD.cListaEncad import cLista


class cPatio:

    # Inicia com os seguintes atributos:

    def __init__(self, nome, qntPilhas, alturaMax):

        if alturaMax > 9:       # Redefine a altura maxima de empilhamento entre 6-9
            alturaMax = 9
        elif alturaMax < 6:
            alturaMax = 6

        self.__nome = nome

        self.__pilhaP1 = cLista()
        self.__pilhaP2 = cLista()
        self.__pilhaP3 = cLista()
        self.__pilhaP4 = cLista()

        self.__qntPilhas = qntPilhas
        self.__alturaMax = alturaMax

        for i in range(qntPilhas):                          # Cria pilhas de prioridade dentro de todas as listas
            self.__pilhaP1.insereDadoFinal(cPilha())
            self.__pilhaP2.insereDadoFinal(cPilha())
            self.__pilhaP3.insereDadoFinal(cPilha())
            self.__pilhaP4.insereDadoFinal(cPilha())

# *******************************************************

    def __str__(self):          # print que mostra todos os atributos e suas pilhas 

        outStr = ""

        outStr += "=========== PATIO ===========\n"
        outStr += f"NOME: {self.__nome}\n"
        outStr += f"QTD PILHAS POR PRIORIDADE: {self.__qntPilhas}\n"
        outStr += f"ALTURA MAXIMA DAS PILHAS: {self.__alturaMax}\n"
        outStr += f"CAPACIDADE TOTAL: {self.getCapacidade()}\n"
        outStr += f"TOTAL CONTAINERS: {self.getTotalContainers()}\n\n"

        outStr += "----- PRIORIDADE 4 | PERECIVEL -----\n"

        no = self.__pilhaP4.getInicio()

        contador = 1

        while no != None:

            pilha = no.getDado()

            outStr += f"PILHA P4-{contador}: "
            outStr += f"{pilha}\n"

            contador += 1
            no = no.getProx()

        outStr += "\n"

        outStr += "----- PRIORIDADE 3 | URGENTE -----\n"

        no = self.__pilhaP3.getInicio()

        contador = 1

        while no != None:

            pilha = no.getDado()

            outStr += f"PILHA P3-{contador}: "
            outStr += f"{pilha}\n"

            contador += 1
            no = no.getProx()

        outStr += "\n"

        outStr += "----- PRIORIDADE 2 | MISTO -----\n"

        no = self.__pilhaP2.getInicio()

        contador = 1

        while no != None:

            pilha = no.getDado()

            outStr += f"PILHA P2-{contador}: "
            outStr += f"{pilha}\n"

            contador += 1
            no = no.getProx()

        outStr += "\n"

        outStr += "----- PRIORIDADE 1 | NAO PERECIVEL -----\n"

        no = self.__pilhaP1.getInicio()

        contador = 1

        while no != None:

            pilha = no.getDado()

            outStr += f"PILHA P1-{contador}: "
            outStr += f"{pilha}\n"

            contador += 1
            no = no.getProx()

        outStr += "\n"

        return outStr

# *******************************************************

    # getters que retornam os atributos

    def getCapacidade(self):
        return self.__qntPilhas * self.__alturaMax * 4

    def getNome(self):
        return self.__nome
    
    def getAlturaMax(self):
        return self.__alturaMax
    
    def getQtdPilhas(self):
        return self.__qntPilhas

# *******************************************************

    # função que retorna se o patio esta vazio

    def patioVazio(self): 
        if (self.pilhaP1Vazia() == None and
            self.pilhaP2Vazia() == None and
            self.pilhaP3Vazia() == None and
            self.pilhaP4Vazia() == None):
            return True
        else:
            return False
    
# *******************************************************
    
    # função que retorna o total de containers do patio

    def getTotalContainers(self):

        total = 0

        total += self.getTotalContainersP1()
        total += self.getTotalContainersP2()
        total += self.getTotalContainersP3()
        total += self.getTotalContainersP4()

        return total
    
# *******************************************************

    # função que verifica se tem espaço no patio

    def verifica_espaco(self):

        if self.getTotalContainers() < self.getCapacidade():
            return True
        else: 
            return False
    
# *******************************************************
    #
    ## Função de armazenar container no patio de acordo com a prioridade

    def armazenar(self, container):

        if self.getTotalContainers() == self.getCapacidade(): ## Verifica se esta cheio
            return False

        ## Verifica a prioridade e adiciona na pilha ( faz isso com todas as prioridades )
        if container.getPrioridade() == 4:  

            pilha = self.verificaP4Cheia()

            if pilha != False:
                pilha.push(container)
                return True
            return False
        
        elif container.getPrioridade() == 3:

            pilha = self.verificaP3Cheia()

            if pilha != False:
                pilha.push(container)
                return True
            return False
        
        elif container.getPrioridade() == 2:

            pilha = self.verificaP2Cheia()

            if pilha != False:
                pilha.push(container)
                return True
            return False
        
        else:
            
            pilha = self.verificaP1Cheia()

            if pilha != False:
                pilha.push(container)
                return True
            return False

    ## Função para librear container para a doca
    def liberar(self, prioridade):

        ## verifica a prioridade e retorna seu respectivo container
        if prioridade == 4:

            pilha = self.pilhaP4Vazia()

            if pilha != None:
                return pilha.pop()

        elif prioridade == 3:

            pilha = self.pilhaP3Vazia()

            if pilha != None:
                return pilha.pop()

        elif prioridade == 2:

            pilha = self.pilhaP2Vazia()

            if pilha != None:
                return pilha.pop()

        else:

            pilha = self.pilhaP1Vazia()

            if pilha != None:
                return pilha.pop()

        return None
        
# ************************************************************************************#
# ******** ABAIXO TODAS AS VERIFICAÇÕES DE TODAS AS LISTAS POR PRIORIDADE ************#
# ************************************************************************************#

    def pilhaP1Vazia(self):

        no = self.__pilhaP1.getInicio()

        while no != None:

            pilha = no.getDado()

            if not pilha.empty():
                return pilha

            no = no.getProx()

        return None

# *******************************************************

    def pilhaP2Vazia(self):

        no = self.__pilhaP2.getInicio()

        while no != None:

            pilha = no.getDado()

            if not pilha.empty():
                return pilha

            no = no.getProx()

        return None
    
# *******************************************************

    def pilhaP3Vazia(self):

        no = self.__pilhaP3.getInicio()

        while no != None:

            pilha = no.getDado()

            if not pilha.empty():
                return pilha

            no = no.getProx()

        return None
# *******************************************************

    def pilhaP4Vazia(self):

        no = self.__pilhaP4.getInicio()

        while no != None:

            pilha = no.getDado()

            if not pilha.empty():
                return pilha

            no = no.getProx()

        return None
        
# *******************************************************

    def getTotalContainersP1(self):

        total = 0
        no = self.__pilhaP1.getInicio()

        while no != None:

            pilha = no.getDado()

            total += pilha.getTamanho()

            no = no.getProx()

        return total

# *******************************************************
    
    def getTotalContainersP2(self):

        total = 0
        no = self.__pilhaP2.getInicio()

        while no != None:

            pilha = no.getDado()

            total += pilha.getTamanho()

            no = no.getProx()

        return total

# *******************************************************

    def getTotalContainersP3(self):

        total = 0
        no = self.__pilhaP3.getInicio()

        while no != None:

            pilha = no.getDado()

            total += pilha.getTamanho()

            no = no.getProx()

        return total

# *******************************************************
    
    def getTotalContainersP4(self):

        total = 0
        no = self.__pilhaP4.getInicio()

        while no != None:

            pilha = no.getDado()

            total += pilha.getTamanho()

            no = no.getProx()

        return total

# *******************************************************

    def verificaP1Cheia(self):

        no = self.__pilhaP1.getInicio()

        while no != None:

            pilha = no.getDado()

            if pilha.getTamanho() < self.getAlturaMax():
                return pilha

            no = no.getProx()
        
        return False

# *******************************************************
   
    def verificaP2Cheia(self):

        no = self.__pilhaP2.getInicio()

        while no != None:

            pilha = no.getDado()

            if pilha.getTamanho() < self.getAlturaMax():
                return pilha

            no = no.getProx()
        
        return False

# *******************************************************

    def verificaP3Cheia(self):

        no = self.__pilhaP3.getInicio()

        while no != None:

            pilha = no.getDado()

            if pilha.getTamanho() < self.getAlturaMax():
                return pilha

            no = no.getProx()
        
        return False

# *******************************************************

    def verificaP4Cheia(self):

        no = self.__pilhaP4.getInicio()

        while no != None:

            pilha = no.getDado()

            if pilha.getTamanho() < self.getAlturaMax():
                return pilha

            no = no.getProx()
        
        return False