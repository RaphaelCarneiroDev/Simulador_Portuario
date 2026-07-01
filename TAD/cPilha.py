##
## TAD de PILHA para organização de containers baseado no TAD: lista Encadeada ( TAD/cListaEncad.py )
##

from TAD.cListaEncad import cLista

class cPilha:

    def __init__(self):             ## Pilha inicia como uma lista Encadeada
        self.__lista = cLista()

    def __str__(self):              ## Print da Pilha ultiliza o str (print) da lista Encadeada
        return str(self.__lista)

    def push(self, n):              ## push para adicionar um elemento na pilha, ultiliza o método de inserir no final da lista
        self.__lista.insereDadoFinal(n)

    def pop(self):                  ## pop para remover o ultimo elemento da pilha e retornar o valor, ultiliza o método de remover do final da lista
        valor = self.__lista.removedadoFinal()
        return valor
    
    def empty(self):                ## empty para verificar se a pilha está vazia, ultilza o método de verificar se a lista está vazia
        return self.__lista.listaVazia()
    
    def getTamanho(self):           ## getTamanho para retornar o tamanho da pilha
        return self.__lista.getTamanho()
    
    def getTopo(self):              ## getTopo para retornar o nó no topo da lista
        return self.__lista.getFim()
    
    def resumo(self):               ## resumo para imprimir somente o tamanho da pilha, ultilizado para imprimir somente a quantidade de containers
        return f"{self.getTamanho()} containers"
    
