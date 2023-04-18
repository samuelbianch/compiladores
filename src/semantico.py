
class AnalisadorSemantico():

    def __init__(self, lista_tokens):
        self.lista_tokens = lista_tokens

    def divisao_por_zero(self, linha):
        # str(linha.replace(" ", ""))
        if linha in "'":
            return False
        if linha in "/0":
            return True

    def analisa(self):
        #tamanho_lista = len(self.lista_tokens)
        print(self.lista_tokens)
        i = 0

        while self.lista_tokens:
            if self.divisao_por_zero(self.lista_tokens[i]):
                print("Erro semântico: divisão por zero")
                exit(0)
            
            i += 1
