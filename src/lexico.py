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


Tokens 100-199:
100 - leia
101 - escreva
102 - se
103 - senao
104 - enquanto
105 - int


'''


import string

# Delimitadores da linguagem
DELIMITADORES = ";(){}"
LETRA = string.ascii_letters
NUMEROS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
PALAVRA_RESERVADA = "leia escreva se senao enquanto int".split()

class AnalisadorLexico():
    name = "Analisador Léxico"

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

    def is_letter(self, caractere):
        """Verfica se o digito de entrada é uma letra"""

        if caractere in LETRA:
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

        return "token10"+str(position)
    

    def analisa(self, arquivo):
        """Analisador de linha a linha para definir quais digitos/tokens foram encontrados"""

        linha = arquivo.readline()

        linha_atual = 1

        while linha:
            i = 0
            tam_linha = len(linha)

            while i < tam_linha:
                caracter_atual = linha[i]
                caracter_seguinte = None

                # Verifica se o caractere atual não é o final da linha
                if ((i+1) < tam_linha):
                    caracter_seguinte = linha[i+1]

                if (self.is_limiter(caracter_atual)):
                    return "Returnar alguma coisa"
                