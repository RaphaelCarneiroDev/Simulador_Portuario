#
# TAD cListaEncadeada ultilizada como base para os TAD cPilha ( TAD/cPilha.py ) e cFilaPrioridade ( TAD/cFilaPrioridade.py )
# Ultiliza como base o TAD cNo ( TAD/cNo.py )
#

from TAD.cNo import cNo

class cLista:

# *******************************************************

    def __init__(self): ## Lista inicia vazia
        
        self.__inicio = None
        self.__fim    = None
        self.__numElems = 0

# *******************************************************

    def __str__(self): ## Print ultiliza o str (print) do cNo para mostrar todos os 'No' da lista em ordem, ultilizando um print de lista vazia como tratamento

        outStr = ""

        if self.__inicio == None:        
            outStr += "=============\n"
            outStr += "|   VAZIO   |\n"
            outStr += "=============\n"
        else:
            x = self.__inicio
            while x != None:
                outStr += str(x)
                x = x.getProx()

        return outStr

# *******************************************************

    def listaVazia(self): ## Retorna um valor booleano para caso a lista estiver vazia ou nao
        if self.__numElems == 0 and self.__inicio == None:
            return True
        else:
            return False

# *******************************************************

    def getTamanho(self): ## Retorna o tamanho da lista
        return self.__numElems
    
# *******************************************************

    def insereDadoFinal(self, n): ## insere um dado no final da lista
        novoNo = cNo(n)
        if self.__inicio != None:           ## verifica se a lista esta vazia
            self.__fim.setProx(novoNo)      ## Adiciona o novo valor para o proximo 'No' do fim atual
            novoNo.setAnt(self.__fim)       ## Coloca como anterior do novo valor o fim atual
            self.__fim = novoNo             ## Coloca como Fim o valor 
        else:                               ## se estiver vazia coloca o dado como primeiro dado
            self.__inicio = novoNo
            self.__fim = novoNo
        self.__numElems += 1

    def insereDadoInicio(self, n): ## insere um dado no inicio da lista
        novoNo = cNo(n)
        if self.__inicio != None:       ## Verifica se a lista esta vazia
            inicio = self.__inicio      ##  usa uma variavel temporaria para guardar o inicio
            novoNo.setProx(inicio)      ##  adiciona como proximo 'No' do valor o inicio atual
            self.__inicio.setAnt(novoNo)    ## define o anterior do valor como o inicio atual
            self.__inicio = novoNo      ## define o inicio como o valor
        else:                           ## Se estiver vazia coloca como primeiro dado
            self.__inicio = novoNo
            self.__fim = novoNo

        self.__numElems += 1

# *******************************************************

    def buscaDado(self, n):     ## Metodo para buscar um respectivo Dado na lista
            
            x = self.__inicio                           ## usa uma variavel x para percorrer a lista inciando como o primeiro 'No'
            while x != None and x.getDado() != n:       ## Percorre a lista até encontrar o valor ou acabar a lista
                x = x.getProx()
            if x == None:
                return False
            else:
                return True                             ## assim retornando um valor booleano para se caso encontrar ou nao+
            

# *******************************************************

    def removedadoFinal(self):              ## Metodo para remover o ultimo 'No' da lista e retorna o valor

        if self.__inicio == None:           ## verifica se a lista esta vazia e retorna FALSE se estiver
            return False
        auxiliar = self.__fim               ## difine uma varivael temporaria Auxiliar para guardar o ultimo 'No'
        valor = self.__fim.getDado()        ## Salva o valor do 'No' para retornar
        if self.__fim == self.__inicio:     ## se a lista so estiver um 'No', define a lista como vazia
            self.__fim = None
            self.__inicio = None
        else:                               ## Caso passar pelas 2 condições a cima:
            self.__fim = auxiliar.getAnt()  ## Define o fim como o anterior o auxiliar (antigo fim)
            self.__fim.setProx(None)        ## Define o proximo do fim atual como None
        del auxiliar                        ## Deleta o fim antigo
        self.__numElems -= 1                ## diminui o tamanho da lista
        return valor                        ## retorna o valor removido
    
    def removedadoInicio(self):             ## Metodo para remover o primeiro "No" da lista e retornar o valor
        if self.__inicio == None:           ## verifica se a lista esta vazia e retorna FALSE se estiver
            return False
        auxiliar = self.__inicio            ## difine uma varivael temporaria Auxiliar para guardar o primeiro 'No'
        valor = self.__inicio.getDado()     ## Salva o valor do 'No' para retornar
        if self.__inicio == self.__fim:     ## se a lista so estiver um 'No', define a lista como vazia
            self.__inicio = None
            self.__fim = None
        else:                                   ## Caso passar pelas 2 condições a cima:
            self.__inicio = auxiliar.getProx()  ## Define o inicio como o proximo no do auxiliar (inicio atual)
            self.__inicio.setAnt(None)          ## Define o antecessor do inicio como None
        del auxiliar                            ## Deleta o auxiliar (inicio antigo)
        self.__numElems -= 1                    ## Diminui o tamanho da lista
        return valor                            ## Retorna o valor

# *******************************************************

    def getInicio(self):        ## Retorna o inicio
        inicio = self.__inicio
        return inicio

# *******************************************************

    def getFim(self):           ## Retorna o fim
        fim = self.__fim
        return fim
