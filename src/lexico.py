'''
Lista de Tokens

Tokens 0-99:
10 - ;
11 - ->
12 - =
13 - \n


Tokens 100-199:
100 - leia
101 - escreva
102 - se
103 - senao
104 - enquanto
105 - int
106 - =


Tokens 200-299:
200 - 0
201 - 1
202 - 2
203 - 3
204 - 4
205 - 5
206 - 6
207 - 7
208 - 8
209 - 9


Tokens 300-399
300 - +
301 - -
302 - /
303 - *
304 - >
305 - <
306 - ==
307 - !=

Tokens 400-499
400 - id

'''


import string

# Delimitadores da linguagem
DELIMITADORES = ";(){}"
MATEMATICA = "+ - / * > < == !=".split()
LETRA = string.ascii_letters
NUMEROS = "0 1 2 3 4 5 6 7 8 9".split()
PALAVRA_RESERVADA = "leia escreva se senao enquanto int =".split()

class AnalisadorLexico():
    """Classe que analisa o texto de entrada e separa os tokens da linguagem implementada"""

    def __str__(self):
        return self.name

    def is_limiter(self, caracter):
        """Verifica se um digito é delimitador de uma lista de comandos"""
        if caracter in DELIMITADORES:
            return True
        
        return False
    
    def token_limitador(self, entrada):
        """Verifica qual é o token de entrada"""
        position = DELIMITADORES.find(entrada)

        return "tok1"+str(position)

    def is_letra(self, caractere):
        """Verfica se o digito de entrada é uma letra"""

        if caractere in LETRA:
            return True
        
        return False
    
    def is_numero(self, caractere):
        """Verifica se o caracter é um número"""
        # print("entrei aqui")
        if caractere in NUMEROS:
            # print("retornei true")
            return True
        
        return False
    
    def qual_numero(self, entrada):
        """Retorna qual o numero"""
        position = 0
        for entrada in NUMEROS:
            if entrada == NUMEROS:
                break
            
            position

        return "token20" + str(position)
    
    def is_seta(self, entrada):
        """Verifica se a entrada é == ->"""
        if entrada[0] == '-' and entrada[1] == '>':
            return True
        
        return False
    
    def is_palavra_reservada(self, entrada):
        """Verifica se o conjunto de caractere é uma palavra reservada"""
        # print(PALAVRA_RESERVADA)
        if entrada in PALAVRA_RESERVADA:
            # print("Palavra reservada encontrada: " + entrada)
            return True
        
        return False

    def qual_palavra_reservada(self, entrada):
        """Devolve qual o token da palavra reservada"""
        position = 0
        while position < len(PALAVRA_RESERVADA):
            if PALAVRA_RESERVADA[position] == entrada:
                # print("Palavra reservada encontrada: ", PALAVRA_RESERVADA[position])
                break
            position += 1

        return "tok10"+str(position)
    
    def is_math(self, caracter_anterior, entrada, caracter_seguinte):
        """Verifica se é um operador matemático"""
        if self.is_seta(str(entrada) + str(caracter_seguinte)) == True:
            return False
        if caracter_anterior == '-':
            return False
        if entrada in MATEMATICA:
            return True
        elif str(entrada) + str(caracter_seguinte) in MATEMATICA:
            return True
        
        return False
    

    def qual_operador(self, entrada, caracter_seguite):
        """Devolve o token do operador matemático"""
        if caracter_seguite == '=':
            entrada += caracter_seguite
        position = 0
        while position < len(MATEMATICA):
            if MATEMATICA[position] == entrada:
                break
            position += 1

        return "tok30"+str(position)
    
    def is_recebe(self, caracter_anterior, caracter_atual):
        """Verifica se é o operador = (alocação de memória)"""
        if caracter_anterior != '!' and caracter_atual == '=':
            return True
        
        return False
    
    def get_lista_de_tokens(token):
        return lista_

    def analisa(self, arquivo):
        lista_tokens = []
        """Analisador de linha a linha para definir quais digitos/tokens foram encontrados"""

        # Cria o arquivo de saída
        arquivo_saida = open('saida_lexico.txt', 'w')

        # Lendo a linha da entrada
        linha = arquivo.readline()

        linha_atual = 1

        while linha:
            i = 0
            tam_linha = len(linha)
            # print(linha)
            while i < tam_linha:
                caracter_atual = linha[i]
                # print("Caractere atual: ", caracter_atual)
                caracter_seguinte = None

                # Só recebe o caracter seguinte, se ele existir
                if ((i+1) < tam_linha):
                    caracter_seguinte = linha[i+1]

                # Verificando se é um caractere limitador: ;(){}
                if self.is_limiter(caracter_atual):
                    lista_tokens.append(caracter_atual)
                    arquivo_saida.write(self.token_limitador(caracter_atual)+','+caracter_atual + ',' + str(linha_atual) + ',' + str(i+1) + '\n')

                # Verificando se é operador matematico
                if i - 1 != -1:
                    if self.is_math(linha[i-1], caracter_atual, caracter_seguinte):
                        if caracter_seguinte == '=':
                            lista_tokens.append(caracter_atual + caracter_seguinte)
                            arquivo_saida.write(self.qual_operador(caracter_atual, caracter_seguinte) + ',' + caracter_atual + caracter_seguinte + ',' + str(linha_atual) + str(i+1) + '\n')
                        else:
                            lista_tokens.append(caracter_atual)
                            arquivo_saida.write(self.qual_operador(caracter_atual, caracter_seguinte) + ',' + caracter_atual + ',' + str(linha_atual) + ',' + str(i+1) + '\n')
                
                
                # Verificando se é a seta do leia e escreva
                if self.is_seta(str(caracter_atual) + str(caracter_seguinte)):
                    lista_tokens.append(caracter_atual+caracter_seguinte)
                    arquivo_saida.write("tok11" + ',' + caracter_atual + caracter_seguinte + ',' + str(linha_atual) + ',' + str(i+1) + '\n')
                
                # Verificando caracter de alocação em memória
                if i - 1 != -1:
                    if self.is_recebe(linha[i-1], caracter_atual):
                        lista_tokens.append(caracter_atual)
                        arquivo_saida.write("tok12" + ',' + caracter_atual + ',' + str(linha_atual) + ',' + str(i+1) + '\n')

                # TODO
                # Verificando se é um numero   
                if caracter_seguinte != None and self.is_numero(caracter_atual):
                    lista_tokens.append(caracter_atual)
                    arquivo_saida.write(self.qual_numero(caracter_atual) + ',' + caracter_atual + ',' + str(linha_atual) + ',' + str(i+1) + '\n')
                

                # Verificando qual é a palavra reservada se nao for, é um id
                elif self.is_letra(caracter_atual):
                    temp = caracter_atual
                    coluna = i
                    i += 1
                    while i < tam_linha:
                        caracter_seguinte = None
                        caracter_atual = linha[i]

                        if (i+1 < tam_linha):
                            caracter_seguinte = linha[i+1]

                        if (self.is_letra(caracter_atual) or self.is_numero(caracter_atual) or caracter_atual == '-' or caracter_atual == '-'):
                            temp += caracter_atual

                        elif (self.is_limiter(caracter_atual) or caracter_atual == ' ' or caracter_atual == '\t' or caracter_atual == '\r' or caracter_atual == '\n' + ',' + str(i+1)):
                            i -= 1
                            break

                        i += 1

                    if self.is_palavra_reservada(temp):
                        # print("entrei aqui")
                        # print(temp)
                        # print(linha_atual)
                        # print(self.qual_palavra_reservada(temp))
                        lista_tokens.append(temp)
                        arquivo_saida.write(self.qual_palavra_reservada(temp) + ',' + temp + ',' + str(linha_atual) + ',' + str(coluna+1) + '\n')
                    else:
                        lista_tokens.append('id')
                        arquivo_saida.write("tok400" + ',' + temp + ',' + str(linha_atual) + ',' + str(coluna+1) + '\n')

                i += 1 # Incrementando a leitura dos caracteres da linha lida no momento

            linha = arquivo.readline() # Le a proxima linha
            linha_atual += 1
