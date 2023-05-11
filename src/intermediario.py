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
    
    def aloca_espaco_memoria(self):
        string = ""

        i = 0

        while i < len(self.lista_variaveis):
            string += self.lista_variaveis[i] + ": DB 8\n"
            i += 1

        return string
    
    def expressao_pos_fixa(self):
        expressao = None


        return expressao

    def get_expressao_infixa(self):
       return pass

    def gerador_intermediario(self):
        self.lista_variaveis = AnalisadorLexico.get_lista_variaveis_to_intermediario()
        self.remove_repetidos()
        
        with open('../out/saida_lexico.txt', 'r') as arquivo:
            lista = arquivo.readlines()
        print(self.aloca_espaco_memoria())


