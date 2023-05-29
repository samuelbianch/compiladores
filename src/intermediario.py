from lexico import AnalisadorLexico

class GeradorIntermediario():

    def __init__(self, lista_variaveis):
        self.lista_variaveis = []
        self.lista_expressoes_pos_fixa = []
        self.lista_expressoes = []
        self.lista_strings = []

        self.lista_variaveis = AnalisadorLexico.get_lista_variaveis_to_intermediario()
        self.remove_repetidos()
        
        with open('../out/saida_lexico.txt', 'r') as arquivo:
            lista = arquivo.readlines()
            self.get_lista_expressoes(lista)
            self.get_string(lista)
            arquivo.close()

    def remove_repetidos(self):
        lista_aux = []
        for i in self.lista_variaveis:
            if i not in lista_aux:
                lista_aux.append(i)
        
        lista_aux.sort()
        self.lista_variaveis = lista_aux

    def get_string(self, lista):
        i = 0        
        while i < len(lista):
            lista_temp = lista[i].split(',')
            #print(lista_temp)
            if lista_temp[0] == 'tok401':
                self.lista_strings.append(lista_temp[1])

            i += 1

    def get_lista_expressoes(self, lista):
        numeros = '0 1 2 3 4 5 6 7 8 9'.split()
        i = 0
        expressao = ""
        while i < len(lista):
            lista_temp = lista[i].split(',')
            # print("Lista temp: ", lista_temp)

            # Ignora os caracteres após o simbolo do leia
            if lista_temp[1] == '->':
                i += 2
                expressao = ""
                continue

            # Limpa o que ele adicionou antes de um recebe
            if lista_temp[1] == '=':
                i += 1
                expressao = ""
                continue

            # Adiciona os numeros na expressao
            if lista_temp[1] in numeros:
                expressao += lista_temp[1]

            # Verifica se é um operador matemático ou um id
            if (AnalisadorLexico.is_math2(lista_temp[1]) or lista_temp[0] == 'tok400'):
                expressao += lista_temp[1]
                #print("Expressao: ", expressao)

            if lista_temp[1] == '(':
                expressao += '('
            
            if lista_temp[1] == ')':
                expressao += ')'
            
            # Quando chegar em algum caracter limitador e a expressão não for vazia, ele adiciona na lista
            if AnalisadorLexico.is_limiter(self, lista_temp[1]) and lista_temp[1] != '(':
                if expressao:
                    self.lista_expressoes.append(expressao)
                    expressao = ""

            i += 1 

        print("Expressao: ", self.lista_expressoes)
        print("Tamanho Expressao: ", len(self.lista_expressoes))
    
    def aloca_espaco_memoria(self):
        string = self.declara_texto()
        string += "\n\nsection .bss ; declara as variaveis\n"

        i = 0

        while i < len(self.lista_variaveis):
            string += '   ' + self.lista_variaveis[i] + ': RESD ' + '1\n'
            i += 1

        return string
    
    def declara_texto(self):
        string = "section .data ; declara constantes\n"
        i = 0
        while i < len(self.lista_strings):
            string += "   string" + str(i) + ": " + "DB " + "'" + self.lista_strings[i] + "', 10, 0\n"
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

    def declara_section_ponto_texto(self):
       return "\n\nsection .text ; importa scanf e printf do gcc compiler\n   global _main\n   extern _printf\n   extern _scanf"

    def gerador_intermediario(self):
        return self.aloca_espaco_memoria() + self.declara_section_ponto_texto()

