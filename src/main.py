import sys

from lexico import AnalisadorLexico

print(sys.argv[0])

lista_caracteres = ''

with open("../teste.txt", "r") as arquivo:
    lista_caracteres += arquivo.read()

print(lista_caracteres)
cont = 0

analisador = AnalisadorLexico()
for i in lista_caracteres:
    if analisador.is_limiter(i):
        cont += 1

    print (cont)
