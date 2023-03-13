import string

# Delimitadores da linguagem
DELIMITADORES = ";(){}"
LETRA = string.ascii_letters
NUMEROS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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

        for caractere in LETRA:
            return True
        
        return False
    
    