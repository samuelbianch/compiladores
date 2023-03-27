import sys

from lexico import AnalisadorLexico

print(sys.argv[0])

try:
    with open(sys.argv[1], "r") as arquivo:
        print("Arquivo lido")
        analisador = AnalisadorLexico()
        analisador.analisa(arquivo)
except Exception as exception:
    print("Excecao ao ler arquivo", exception)
    raise 
