import sys

class GeradorIntermediario():

    def __init__(self, lista_variaveis):
        self.lista_variaveis = lista_variaveis
        self.lista_expressoes_pos_fixa = []

    def gerador_intermediario(self):
        arquivo =  open(sys.argv[1], 'r')
        linha = arquivo.readline
