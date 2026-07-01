#
#   CLASSE cDoca para Organizar o carregamento e descarregamento de containers
#

from entidades.cPatio import cPatio

class cDoca:

    ## inicia com os seguintes atributos:

    def __init__(self, nome, qtdPilhasPatio, alturaPatio):

        self.__nome = nome

        self.__patio = cPatio(      # Cria o patio referente a doca
            f"PATIO {nome}",
            qtdPilhasPatio,
            alturaPatio
        )

        self.__ocupado = False  ## Define que a doca está vazia entao está: FALSE para Ocupado
        self.__estado = None    ## Estado define se tem algum navio e qual navio 
# *******************************************************

    def __str__(self):  ## Print para mostrar os atributos importantes
        
        outStr = ""

        outStr += "==== DOCA ====\n"
        outStr += f"NOME: {self.getNome()}\n"
        outStr += f"PATIO: {self.__patio.getNome()}\n"

        if self.__ocupado:
            outStr += "STATUS: OCUPADA\n"
            outStr += f"{self.__estado}\n"
        else:
            outStr += "STATUS: LIVRE\n"

        return outStr
    
# *******************************************************

    def docaLivre(self):                ## função para verificar se a doca está livre
        return not self.__ocupado
    
# *******************************************************
    
    ## getters para retornar os atributos

    def getNome(self):
        return self.__nome

    def getEstado(self):
        return self.__estado
    
    def getPatio(self):
        return self.__patio

# *******************************************************

    ## funções de atracar e desatracar Navio
    ## Somente verificando se a Doca está Vazia ou nao
    ## E mudando seu atributo

    def atracarNavio(self, navio):
        if self.__ocupado == False:
            self.__estado = navio
            self.__ocupado = True
            return True
        else:
            return False
    
    def desatracarNavio(self):
        if self.__ocupado == True:
            self.__estado = None
            self.__ocupado = False
            return True
        else:
            return False

# *******************************************************

    # Funções de carregar e descarregar container 

    def carregarContainers(self):

        if self.__estado == None:       # se estiiver vazia, retorna False
            return False

        carregados = 0                  # conta o numero de carregados

        navio = self.__estado           # define o navio como o estado ( quem esta atracado )

        prioridade = navio.getPrioridade()  # pega a prioridade do navio

        while not navio.navioCheio():       # enquanto o navio nao estiver cheio:

            container = self.__patio.liberar(prioridade)    # patio libera um container da mesma prioridade

            if container == None:       # se nao vier nenhum container, para o loop
                break

            navio.embarcar(container) # embarca o container

            carregados += 1

        return carregados
        
    def descarregarContainers(self):

        if self.__estado == None:
            return False

        descarregados = 0
        navio = self.__estado

        while not navio.navioVazio(): ## Enquanto o navio nao estiver vazio

            container = navio.desembarcar() ## desenbarca o container 
            del container                   ## deleta o container desenbarcado

            descarregados += 1
        return descarregados

# *******************************************************

    def prepararDoca(self):     ## função para preparar a Doca, ( carrega e descarrega )

        descarregados = self.descarregarContainers()

        carregados = self.carregarContainers()

        return descarregados, carregados

# *******************************************************

    def resumo(self):       ## uma forma resumida de imprimir os status da doca

        outStr = ""

        outStr += f"DOCA: {self.__nome}\n"

        if self.__ocupado:
            outStr += f"STATUS: OCUPADA\n"
            outStr += f"NAVIO: {self.__estado.getNome()}\n"
        else:
            outStr += "STATUS: LIVRE\n"

        return outStr