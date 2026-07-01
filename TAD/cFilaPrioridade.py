#
# TAD cFilaPrioridade para criação de Fila de navios por ordem de prioridade ultilizando o TAD cLista ( TAD/cListaEncad.py )
#

from TAD.cListaEncad import cLista

class cFilaPrioridade:

    def __init__(self): ## Inicia com 4 listas, divididas por prioridade

        self.__filaP4 = cLista()
        self.__filaP3 = cLista()
        self.__filaP2 = cLista()
        self.__filaP1 = cLista()
    
    def __str__(self): ## Print ultiliza o str (print) da lista encadeada para mostar todas as listas

        outStr = ""

        outStr += f"P4: {self.__filaP4.getTamanho()} navios\n"
        outStr += f"P3: {self.__filaP3.getTamanho()} navios\n"
        outStr += f"P2: {self.__filaP2.getTamanho()} navios\n"
        outStr += f"P1: {self.__filaP1.getTamanho()} navios\n"

        return outStr
    
    def queue(self, navio): ## Metodo para adicionar um navio na fila

        prioridade = navio.getPrioridade()      ## Pega a prioridade do navio 

        ## Verifica qual prioridade equivale com a lista e adiciona no final

        if prioridade == 4:
            self.__filaP4.insereDadoFinal(navio)

        elif prioridade == 3:
            self.__filaP3.insereDadoFinal(navio)

        elif prioridade == 2:
            self.__filaP2.insereDadoFinal(navio)

        else:
            self.__filaP1.insereDadoFinal(navio)
    
    def dequeue(self): ## Metodo para remover o proximo navio da fila por ordem de prioridade retornado o valor
        
        ##  Verifica por ordem de prioridade ( começando pela 4 ) qual lista ainda nao esta vazia e remove o primeiro dado ( navio )

        if not self.__filaP4.listaVazia():
            return self.__filaP4.removedadoInicio()

        elif not self.__filaP3.listaVazia():
            return self.__filaP3.removedadoInicio()

        elif not self.__filaP2.listaVazia():
            return self.__filaP2.removedadoInicio()

        elif not self.__filaP1.listaVazia():
            return self.__filaP1.removedadoInicio()

        return None
    
    def empty(self): ## Retorna se todas as listas dentro da fila estiver vazia

        return (
            self.__filaP4.listaVazia() and
            self.__filaP3.listaVazia() and
            self.__filaP2.listaVazia() and
            self.__filaP1.listaVazia()
        )
 
    def getTamanho(self): ## Retorna o tamanho de todas as listas somadas

        return (
            self.__filaP4.getTamanho() +
            self.__filaP3.getTamanho() +
            self.__filaP2.getTamanho() +
            self.__filaP1.getTamanho()
        )