#
# CLASSE cNavio 
#


from TAD.cPilha import cPilha
from TAD.cListaEncad import cLista

class cNavio:

    ## Inicia com os seguintes atributos:

    def __init__(self, nome, empresa, prioridade, qtdPilhas, alturaMax):

        if alturaMax > 5:       ## ajeita a altura para a quantidade minima e maxima de empilhamento de container no navio
            alturaMax = 5
        elif alturaMax < 4:
            alturaMax = 4

        self.__nome = nome
        self.__empresa = empresa
        self.__prioridade = prioridade
        self.__qtdPilhas = qtdPilhas
        self.__alturaMax = alturaMax

        self.__pilhas = cLista()

        for i in range(qtdPilhas):                      ## cria todas as pilhas em uma lista
            pilha = cPilha()
            self.__pilhas.insereDadoFinal(pilha)

# *******************************************************

    def __str__(self):          ## print dos atributos do navio e suas pilhas

        outStr = ""

        outStr += f"NAVIO: {self.__nome}\n"
        outStr += f"EMPRESA: {self.__empresa}\n"
        outStr += f"PRIORIDADE: {self.getPrioridadeStr()}\n"
        outStr += f"PILHAS: {self.__qtdPilhas}\n"
        outStr += f"ALTURA MAX: {self.__alturaMax}\n"
        outStr += f"CAPACIDADE TOTAL: {self.getCapacidadeTotal()}\n\n"

        no = self.__pilhas.getInicio()

        contador = 1

        while no != None:

            pilha = no.getDado()

            outStr += f"PILHA {contador}: {pilha}\n"

            contador += 1
            no = no.getProx()

        return outStr

# *******************************************************

    ## getters dos atributos
    
    def getNome(self):
        return self.__nome

    def getEmpresa(self):
        return self.__empresa

    def getPrioridade(self):
        return self.__prioridade
    
    def getQtdPilhas(self):
        return self.__qtdPilhas
    
    def getAlturaMax(self):
        return self.__alturaMax

    def getPrioridadeStr(self):             ## Converte a prioridade como número para string ( 4 = PERECIVEL ) 
        if self.__prioridade == 4:  
            return 'PERECIVEL'
        elif self.__prioridade == 3:
            return 'URGENTE'
        elif self.__prioridade == 2:
            return "MISTO"
        else:
            return "NAO PERECIVEL"
        
# *******************************************************

    def getCapacidadeTotal(self):                      # retorna a capacidade total do navio ( quantidade de pilhas * altura maxima )
        return self.__qtdPilhas * self.__alturaMax
    
# *******************************************************

    def embarcar(self, container):                              # função para embarcar navio

        if container.getPrioridade() != self.__prioridade:      # se a prioridade do navio e do container nao forem iguais, retorna FAlse
            return False

        no = self.__pilhas.getInicio()

        while no != None:                       # percorre toda a lista de pilhas

            pilha = no.getDado()

            if pilha.getTamanho() < self.__alturaMax:       # se a pilha atual nao estiver cheia, adiciona o container

                pilha.push(container)
                return True

            no = no.getProx()                               # se estiver cheia, vai para a proxima pilha

        return False

    def desembarcar(self):                    # Função para desembarcar navio

        no = self.__pilhas.getInicio()

        while no != None:                     # Percorre toda a lista de pilhas

            pilha = no.getDado()

            if not pilha.empty():             # se ela nao estiver vazia, remove o container e retorna qual foi
                return pilha.pop()

            no = no.getProx()                 # se estiver vazia, vai para a proxima pilha

        return None

# *******************************************************

    def navioVazio(self):               # função de verificação para navio vazio, percorre todas as pilhas e retorna

        no = self.__pilhas.getInicio()

        while no != None:

            pilha = no.getDado()

            if not pilha.empty():
                return False

            no = no.getProx()

        return True
    
# *******************************************************
    def navioCheio(self):                   # função de verificação para navio cheio, percorre todas as pilhas e retorna

        no = self.__pilhas.getInicio()

        while no != None:

            pilha = no.getDado()

            if pilha.getTamanho() < self.__alturaMax:
                return False

            no = no.getProx()

        return True

# *******************************************************

    ## resumos de print para o navio e suas pilhas

    def resumo(self):

        outStr = ""

        outStr += f"NAVIO: {self.__nome}\n"
        outStr += f"EMPRESA: {self.__empresa}\n"
        outStr += f"PRIORIDADE: {self.getPrioridadeStr()}\n"
        outStr += f"CAPACIDADE: {self.getCapacidadeTotal()}\n"

        ocupados = 0

        no = self.__pilhas.getInicio()

        while no != None:

            pilha = no.getDado()

            ocupados += pilha.getTamanho()

            no = no.getProx()

        outStr += f"CONTAINERS: {ocupados}\n"

        return outStr
    
    def resumoPilhas(self):

        outStr = ""

        no = self.__pilhas.getInicio()

        contador = 1

        while no != None:

            pilha = no.getDado()

            outStr += f"PILHA {contador}: "

            if pilha.empty():

                outStr += "VAZIA"

            else:

                topo = pilha.getTopo()

                while topo != None:

                    container = topo.getDado()

                    outStr += f"[{container.getID()}] "

                    topo = topo.getAnt()

            outStr += "\n"

            contador += 1
            no = no.getProx()

        return outStr

    
    