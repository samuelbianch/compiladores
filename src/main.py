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
            analisador_lexico = AnalisadorLexico()
            analisador_lexico.analisa(arquivo)
            arquivo.close()
            
            analisador_sintatico = AnalisadorSintatico(analisador_lexico.get_lista_de_tokens())
            analisador_sintatico.analisa()

            analisador_semantico = AnalisadorSemantico()
            analisador_semantico.analisa()

            gerador_intermediario = GeradorIntermediario(analisador_lexico.get_lista_variaveis())
            to_gerador_codigo = gerador_intermediario.gerador_intermediario()

            gerador_codigo = GeradorCodigo(to_gerador_codigo)
            gerador_codigo.main()

            
    except Exception as exception:
        print("Excecao ao ler arquivo", exception)
        raise 

print("----------- Compilação finalizada! -----------")