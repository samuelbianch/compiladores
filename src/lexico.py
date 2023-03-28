'''
Lista de Tokens

Tokens 0-99:
0 - ;
1 - ->
2 - (
3 - )
4 - <
5 - >
6 - ==
7 - =
8 - {
9 - }
10 - '
11 - !=
12 - \n


Tokens 100-199:
100 - leia
101 - escreva
102 - se
103 - senao
104 - enquanto
105 - int


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
300 -  


'''


import string

# Delimitadores da linguagem
DELIMITADORES = ";(){}"
LETRA = string.ascii_letters
NUMEROS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
PALAVRA_RESERVADA = "leia escreva se senao enquanto int".split()

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
        if caractere in NUMEROS:
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
        if entrada[0] == '-' and entrada[1] == '>':
            return True
        
        return False
    
    def is_palavra_reservada(self, entrada):
        """Verifica se o conjunto de caractere é uma palavra reservada"""
        if entrada in PALAVRA_RESERVADA:
            return True
        
        return False

    def qual_palavra_reservada(self, entrada):
        """Devolve qual o token da palavra reservada"""
        position = 0
        for c in PALAVRA_RESERVADA:
            if c == entrada:
                break

            position += 1

        return "tok10"+str(position)
    

    def analisa(self, arquivo):
        """Analisador de linha a linha para definir quais digitos/tokens foram encontrados"""

        # Cria o arquivo de saída
        arquivo_saida = open('saida.txt', 'w')

        # Lendo a linha da entrada
        linha = arquivo.readline()

        linha_atual = 1

        while linha:
            i = 0
            tam_linha = len(linha)
            print(linha)
            while i < tam_linha:
                caracter_atual = linha[i]
                print("Caractere atual: ", caracter_atual)
                caracter_seguinte = None

                # Só recebe o caracter seguinte, se ele existir
                if ((i+1) < tam_linha):
                    caracter_seguinte = linha[i+1]

                # Verificando se é um caractere limitador -> ;(){}
                if (self.is_limiter(caracter_atual)):
                    arquivo_saida.write(self.token_limitador(caracter_atual)+'_'+caracter_atual + '->' + str(linha_atual) + '\n')

                # Verificando qual é a palavra reservada
                elif (self.is_letra(caracter_atual)):
                    temp = caracter_atual
                    i += 1
                    while i < tam_linha:
                        caracter_seguinte = None
                        caracter_atual = linha[i]

                        if (i+1 < tam_linha):
                            caracter_seguinte = linha[i+1]

                        if (self.is_letra(caracter_atual) or self.is_numero(caracter_atual) or caracter_atual == '_' or caracter_atual == '-'):
                            temp += caracter_atual

                        elif (self.is_limiter(caracter_atual) or caracter_atual == '\n'):
                            i -= 1
                            break

                        i += 1

                    if (self.is_palavra_reservada(temp)):
                        arquivo_saida.write(self.qual_palavra_reservada(temp) + '_' + temp + '->' + str(linha_atual) + '\n')
                        i = linha_atual

                # Verificando se é um numero   
                elif caracter_seguinte != None and self.is_numero(caracter_atual):
                    temp = caracter_atual
                    while (self.is_numero(caracter_atual) and (i+1 < tam_linha)):
                        temp += caracter_atual
                        i += 1
                        caracter_atual = linha[i]
                    arquivo_saida.write(self.qual_numero(caracter_atual + caracter_seguinte) + '_' + temp + '->' + str(linha_atual) + '\n')


                
                i += 1 # Incrementando a leitura dos caracteres da linha lida no momento

            linha = arquivo.readline() # Le a proxima linha
            linha_atual += 1
