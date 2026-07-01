#
# CLASSE cPorto
#


from TAD.cListaEncad import cLista
from TAD.cFilaPrioridade import cFilaPrioridade

class cPorto:

    def __init__(self):             ## Inicia com uma lista de docas e uma fila de espera
        self.__docas  = cLista()
        self.__espera = cFilaPrioridade()

# *******************************************************

    def __str__(self):          ## print com os atributos, docas e fila de espera
        outStr = "" 

        outStr += f" ==== PORTO ====\n"
        outStr += f" ==== DOCAS ====\n"
        noDoca = self.__docas.getInicio()

        while noDoca != None:

            doca = noDoca.getDado()

            outStr += doca.resumo()
            outStr += "\n"

            noDoca = noDoca.getProx()

        outStr += f" ==== FILA DE ESPERA ==== \n"
        outStr += f"{str(self.__espera)}\n"

        return outStr

# *******************************************************

    # funções para cadastrar docas e navios, inserindo em sua respectiva lista/fila

    def cadastrarDoca(self, doca):
        self.__docas.insereDadoInicio(doca)

    def cadastrarNavio(self, navio):
        self.__espera.queue(navio)

# *******************************************************

    def buscaDoca(self, doca):                  # Função que busca uma doca desejada
        return self.__docas.buscaDado(doca)
    
# *******************************************************

    def liberarNavio(self, doca):                               # função que atraca o proximo navio da lista
        if not self.__espera.empty() and doca.docaLivre():      # se a doca estiver livre e estiver um navio na lista
            navio = self.__espera.dequeue()                     # retira o navio da lista de espera ( pela prioridade )
            doca.atracarNavio(navio)                            # atraca o navio
            print(f"{navio.getNome()} ATRACOU NA {doca.getNome()}")
            return True
        return False

# *******************************************************
  
    def buscarDocaLivre(self):                  # Função que percorre toda a lista de docas e retorna qual delas esta livre

        noDoca = self.__docas.getInicio()

        while noDoca != None:

            doca1 = noDoca.getDado()

            if doca1.docaLivre():
                return doca1
            
            noDoca = noDoca.getProx()

        return False
    
    def existeDocaOcupada(self):            # Função que percorre toda a lista e verifica se as docas estao ocupadas

        noDoca = self.__docas.getInicio()

        while noDoca != None:

            doca = noDoca.getDado()

            if not doca.docaLivre():
                return True

            noDoca = noDoca.getProx()

        return False

# *******************************************************

    def processarDoca(self, doca):          # função para processar a doca

        if doca.docaLivre():                # se a doca estiver livre, libera o navio da lista
            self.liberarNavio(doca)
        
        if doca.docaLivre():                # se não, retorna false
            return False

        resultado = doca.prepararDoca()     # define resultado como return do preparar doca, que pode retornar False/True 
                                            # e o valor de carregados e descarregados
        if resultado == False:
            return False

        descarregados, carregados = resultado

        navio = doca.getEstado()

        # Print da doca apos processar

        print(f"NAVIO {navio.getNome()} | {navio.getPrioridadeStr()} PROCESSADO")
        print(f"CONTAINERS DESCARREGADOS: {descarregados}")
        print(f"CONTAINERS CARREGADOS: {carregados}")
        print(f"{navio.resumoPilhas()}")

        doca.desatracarNavio()

        self.liberarNavio(doca)

        return True

# *******************************************************
            
    def verificaFila(self):                     # Função para verificar se tem navio na Fila
        if self.__espera.getTamanho() != 0:
            return True
        return False

# *******************************************************
    def processarPorto(self):                       # Função para proessar o Porto

        ciclo = 1                                   # Conta os ciclos de rotação

        while self.verificaFila() or self.existeDocaOcupada():  # Enquanto houver navio na lista ou todas as docas estiverem ocupadas

            print(f"\n======= CICLO {ciclo} =======\n") # mostra o ciclo atual

            noDoca = self.__docas.getInicio()

            while noDoca != None:   # percorre toda a lista de docas

                doca = noDoca.getDado()

                self.processarDoca(doca)    # processa a doca

                noDoca = noDoca.getProx()

            ciclo += 1