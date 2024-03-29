import sys

from lexico import AnalisadorLexico
from sintatico import AnalisadorSintatico
from semantico import AnalisadorSemantico
from intermediario import GeradorIntermediario
from gerador_codigo import GeradorCodigo

if sys.argv[1]:
    try:
        with open(sys.argv[1], "r") as arquivo:
            print("Arquivo lido")

            DEBUG = False
            if len(sys.argv) > 2:
                if sys.argv[2] == '-tudo':
                    DEBUG = True

            analisador_lexico = AnalisadorLexico(DEBUG)
            analisador_lexico.analisa(arquivo)
            arquivo.close()
            
            analisador_sintatico = AnalisadorSintatico(analisador_lexico.get_lista_de_tokens(), DEBUG)
            analisador_sintatico.analisa()

            analisador_semantico = AnalisadorSemantico(DEBUG)
            analisador_semantico.analisa()

            gerador_intermediario = GeradorIntermediario(DEBUG)
            to_gerador_codigo_basic = gerador_intermediario.gerador_intermediario()
            to_gerador_codigo_lista_expressoes = gerador_intermediario.get_lista_expressoes(analisador_lexico.get_lista_de_tokens())
            to_gerador_codigo_lista_strings = gerador_intermediario.get_string_to_code()

            gerador_codigo = GeradorCodigo(to_gerador_codigo_basic, to_gerador_codigo_lista_expressoes, to_gerador_codigo_lista_strings, DEBUG)
            gerador_codigo.main()

            
    except Exception as exception:
        print("Excecao ao ler arquivo", exception)
        raise 

print("----------- Compilação finalizada! -----------")