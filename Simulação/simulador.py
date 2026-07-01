#
# Modulo simulador.py, onde simmula o porto e imprime o processo
#


import sys

from Simulação.gerador import gerarPorto

def main(): ## função main() ultilizada para guardar a simulação e ser chamada no main.py

    if len(sys.argv) >= 3: ## pega o tamanho da entrada e se for maior ou igual 3:

        qtdDocas = int(sys.argv[1]) ## define a quantidade de docas na 2 palavra da entrada
        qtdNavios = int(sys.argv[2]) ## define a quantidade de navios na 3 palavra da entrada

    else:   ## se for menor do que 3:

        qtdDocas = 3      ## define a quantidade de docas por default igual a 3
        qtdNavios = 10    ## define a quantidade de navios por default igual a 10

    porto = gerarPorto(qtdDocas, qtdNavios) ## Gera o Porto com as quantidades selecionadas

    print(porto ) ## Mostra o porto antes do processamento

    print("PROCESSANDO PORTO...\n")

    porto.processarPorto() ## Processa o porto

    print("\nPORTO APÓS PROCESSAMENTO:\n")

    print(porto) ## Mostra o Porto depois do processamento

    print("\nSIMULAÇÃO FINALIZADA")

if __name__ == "__main__":
    main()