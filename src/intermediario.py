from lexico import AnalisadorLexico

class GeradorIntermediario():

    def __init__(self, lista_variaveis):
        self.lista_variaveis = []
        self.lista_expressoes_pos_fixa = []
        self.lista_expressoes = []

    def remove_repetidos(self):
        lista_aux = []
        for i in self.lista_variaveis:
            if i not in lista_aux:
                lista_aux.append(i)
        
        lista_aux.sort()
        self.lista_variaveis = lista_aux

    def get_lista_expressoes(self, lista):
        i = 0
        expressao = ""
        while i < len(lista):
            posicao = 0
            lista_temp = lista[i].split(',')
            print("Lista temp: ", lista_temp)
            if AnalisadorLexico.is_math2(lista_temp[1]) and not AnalisadorLexico.is_limiter(self, lista_temp[1]):
                expressao += lista_temp[1]
            elif AnalisadorLexico.is_limiter(self, lista_temp[1]):
                if not expressao:
                    self.lista_expressoes.append(expressao)
                    expressao = ""

            i += 1 

        print(self.lista_expressoes)
    
    def aloca_espaco_memoria(self):
        string = ""

        i = 0

        while i < len(self.lista_variaveis):
            string += self.lista_variaveis[i] + ": DB 8\n"
            i += 1

        return string
    
    def expressao_pos_fixa(self):
        expressao = None
        i = 0
        while i < self.lista_expressoes:
            expressao 
            self.lista_expressoes_pos_fixa[i] = expressao
            i += 1

        return expressao

    def get_expressao_infixa(self):
       return None

    def gerador_intermediario(self):
        self.lista_variaveis = AnalisadorLexico.get_lista_variaveis_to_intermediario()
        self.remove_repetidos()
        
        with open('../out/saida_lexico.txt', 'r') as arquivo:
            lista = arquivo.readlines()
            self.get_lista_expressoes(lista)
            arquivo.close()
        print(self.aloca_espaco_memoria())


