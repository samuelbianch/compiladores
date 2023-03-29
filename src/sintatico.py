''' LISTA DE COMANDOS
0 - 	<PROGRAM> ::= <STMT_LIST>
1 - 	<STMT_LIST> ::= <STMT> ";" <STMT_LIST>
2 - 	<STMT_LIST> ::= î
3 - 	<STMT> ::= read "->" id
4 - 	<STMT> ::= write "->" <MESSAGE>
5 - 	<STMT> ::= <IF>
6 - 	<STMT> ::= <GET>
7 - 	<STMT> ::= <WHILE>
8 - 	<MESSAGE> ::= id
9 - 	<MESSAGE> ::= string
10 - 	<MESSAGE> ::= î
11 - 	<MESSAGE> ::= "\n"
12 - 	<GET> ::= id atribute <EXPRESSION>
13 - 	<IF_ELSE> ::= î
14 - 	<IF_ELSE> ::= <ELSE>
15 - 	<IF> ::= if "(" <COMP> ")" "{" <STMT_LIST> "}" <IF_ELSE>
16 - 	<ELSE> ::= else "{" <STMT_LIST> "}"
17 - 	<EXPRESSION> ::= <TERM> <TERM_TAIL>
18 - 	<TERM_TAIL> ::= <PLUS_MINUS> <TERM> <TERM_TAIL>
19 - 	<TERM_TAIL> ::= î
20 - 	<TERM> ::= <FACTOR> <FACTOR_TAIL>
21 - 	<FACTOR_TAIL> ::= <MULT_OPERATOR> <FACTOR> <FACTOR_TAIL>
22 - 	<FACTOR_TAIL> ::= î
23 - 	<FACTOR> ::= "(" <EXPRESSION> ")"
24 - 	<FACTOR> ::= id
25 - 	<FACTOR> ::= number
26 - 	<RELATIONAL_OPERATOR> ::= ">"
27 - 	<RELATIONAL_OPERATOR> ::= "<"
28 - 	<RELATIONAL_OPERATOR> ::= "=="
29 - 	<RELATIONAL_OPERATOR> ::= "!="
30 - 	<MULT_OPERATOR> ::= mult
31 - 	<MULT_OPERATOR> ::= div
32 - 	<PLUS_MINUS> ::= plus
33 - 	<PLUS_MINUS> ::= minus
34 - 	<COMP> ::= <EXPRESSION> <RELATIONAL_OPERATOR> <EXPRESSION>
35 - 	<WHILE> ::= while "(" <COMP> ")" "{" <STMT_LIST> "}"
'''
import string
from typing import List

class AnalisadorSintatico():
    nome = "Analisador Sintatico"

    def analisa(self, lista_tokens):
        """Analisador Sintatico"""
        pilha_comandos: List[str] = []
        pilha_lexico: List[str] = []
        
        pilha_comandos.append('$')
        pilha_comandos.append('PROGRAM')
        pilha_comandos.append('STMT_LIST')

        #with open("..\teste.txt", 'r') as arquivo:
        
        #pilha_lexico.append()

        print(lista_tokens)
        pilha_comandos.pop()
        saida = open('saida_sintatico.txt', 'w')
        saida.write(str(pilha_comandos))
        # print(arquivo.readline())