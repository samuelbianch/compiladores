
class AnalisadorSemantico():

    def __init__(self):
       pass

    def divisao_por_zero(self, lista):
        i = 0
        # print("Verifiquei se a divisao é por zero")
        while len(lista) > i:
            x = lista[i]
            lista_temp = x.split(",")
            if 'tok302' in lista_temp:
                x = lista[i+1]
                lista_temp = x.split(",")
                if 'tok200' in lista_temp:
                    print("ERRO! Divisão por zero, linha: " + str(lista_temp[2]) + " coluna: " + str(lista_temp[3]))
                    exit(0)
            i += 1

    def analisa(self):
        with open('D:\\apps\compiladores\out\saida_lexico.txt', 'r') as arquivo:
            lista = arquivo.readlines()
            self.divisao_por_zero(lista)
