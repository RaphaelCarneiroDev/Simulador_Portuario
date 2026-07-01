#
# TAD cNo para servir como base dos proximos TAD, principalmente da Lista Encadeada ( TAD/ListaEncad.py )
#

class cNo:

    # *******************************************************

    def __init__(self, dado = 0):  ## cNo inicia com o dado estando em 0 como default 
        
        self.__dado = dado 
        self.__prox = None
        self.__ant  = None
    
    # *******************************************************

    def __str__(self): ## Print do 'No' seguindo como base uma lista encadeada, com ponteiros guiando para o proximo 'No' 

        outStr = ""

        if self:
  
            outStr += f'| {self.__dado} | \n'

            outStr +=  " |   \n"
            if self.__prox:
                outStr +=  " V  \n"
            else:
                outStr +=  "===  \n"
  
        return outStr
    
    # *******************************************************
    
    def setDado(self, dado):    ## setDado para mudar o valor de um 'No'

        self.__dado = dado
    
    def setProx(self, prox):    ## setProx para mudar o próximo 'No' de um respectivo 'No'

        if type(prox) == cNo:
            self.__prox = prox
        else:
            self.__prox = None

    def setAnt(self, ant):      ## setAnt para mudar o 'No' anterior de um respectivo 'No'

        if type(ant) == cNo:
            self.__ant = ant
        else:
            self.__ant = None

    # *******************************************************

    ## Metodos para retornar o 'No' e seus sucessores e antecessores  
    
    def getDado(self):
        return self.__dado
    
    def getProx(self):
        return self.__prox
    
    def getAnt(self):
        return self.__ant
    
    # *******************************************************