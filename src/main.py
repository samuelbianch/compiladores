import sys

from lexico import AnalisadorLexico
from sintatico import AnalisadorSintatico

try:
    with open(sys.argv[1], "r") as arquivo:
        print("Arquivo lido")
        analisador_lexico = AnalisadorLexico()
        analisador_lexico.analisa(arquivo)
        arquivo.close()
        analisador_sintatico = AnalisadorSintatico()
        analisador_sintatico.analisa(analisador_lexico.get_lista_de_tokens)
except Exception as exception:
    print("Excecao ao ler arquivo", exception)
    raise 
