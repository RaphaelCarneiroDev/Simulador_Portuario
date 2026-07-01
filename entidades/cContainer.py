#
# CLASSE cContainer para organizar e gerenciar o objeto container
#

class cContainer:

# *******************************************************

    ## Inicia o container com os seguintes atributos:

    def __init__(self, ID, peso, destino, prioridade, empresa, tipo, limitePilha):
        self.__ID = ID
        self.__peso = peso
        self.__destino = destino
        self.__prioridade = prioridade
        self.__empresa = empresa
        self.__limite = limitePilha
        self.__tipo = tipo

# *******************************************************

    ## Print do container, mostrando todos os atributos importantes

    def __str__(self):
        
        outStr = ""
        outStr += "CONTAINER:\n"
        outStr += f"ID: {self.getID()} \n"
        outStr += f"DESTINO: {self.getDestino()} \n"
        outStr += f"PRIORIDADE: {self.getPrioridadeStr()} \n"
        outStr += f"LIMITE: {self.getLimite()} \n"

        return outStr

# *******************************************************

    ## getters dos atributos 

    def getEmpresa(self):
        return self.__empresa
    
    def getTipo(self):
        return self.__tipo
    
    def getID(self):
        return self.__ID

    def getPeso(self):
        return self.__peso

    def getDestino(self):
        return self.__destino

    def getLimite(self):
        return self.__limite

    def getPrioridade(self):
        return self.__prioridade
    def setPrioridade(self, n):
        self.__prioridade = n

    def getPrioridadeStr(self):         ## Converte a prioridade como número para string ( 4 = PERECIVEL )
        if self.__prioridade == 4:
            return 'PERECIVEL'
        elif self.__prioridade == 3:
            return 'URGENTE'
        elif self.__prioridade == 2:
            return "MISTO"
        else:
            return "NAO PERECIVEL"

# *******************************************************

    def resumo(self):                   ## Retorna um print de mandeira resumida, somente o ID e a prioridade

        return f"[{self.__ID} | {self.getPrioridadeStr()}]" 

