from lexico import AnalisadorLexico

class GeradorIntermediario():

    def __init__(self, lista_variaveis):
        self.lista_variaveis = []
        self.lista_expressoes_pos_fixa = []
    
    def remove_repetidos(self):
        lista_aux = []
        for i in self.lista_variaveis:
            if i not in lista_aux:
                lista_aux.append(i)
        
        lista_aux.sort()
        self.lista_variaveis = lista_aux
    
    def gerador_intermediario(self):
        self.lista_variaveis = AnalisadorLexico.get_lista_variaveis_to_intermediario()
        self.remove_repetidos()
        print(self.lista_variaveis)
