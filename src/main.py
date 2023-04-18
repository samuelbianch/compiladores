import sys

from lexico import AnalisadorLexico
from sintatico import AnalisadorSintatico
from semantico import AnalisadorSemantico

if sys.argv[1]:
    try:
        with open(sys.argv[1], "r") as arquivo:
            print("Arquivo lido")
            analisador_lexico = AnalisadorLexico()
            analisador_lexico.analisa(arquivo)
            arquivo.close()
            
            analisador_sintatico = AnalisadorSintatico(analisador_lexico.get_lista_de_tokens())
            analisador_sintatico.analisa()

            analisador_semantico = AnalisadorSemantico(analisador_lexico.get_lista_de_tokens())
            analisador_semantico.analisa()
            
    except Exception as exception:
        print("Excecao ao ler arquivo", exception)
        raise 

print("----------- Compilação finalizada! -----------")