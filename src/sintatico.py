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

class AnalisadorSintatico:

    def __init__(self, lista_tokens):
        self.lista_tokens = lista_tokens
        self.pilha_comandos: List[str] = []
        self.pilha_comandos.append('$')
        self.pilha_comandos.append('<PROGRAM>')

    def empilha(self, elemento):
        self.pilha_comandos.append(elemento)

    def desempilha(self):
        self.pilha_comandos.pop()

    def procedimento(self, opcao):
        if opcao == 0:
            self.desempilha()
            self.empilha('<STMT_LIST>')
        
        elif opcao == 1:
            self.desempilha()
            self.empilha('<STMT_LIST>')
            self.empilha(';')
            self.empilha('<STMT>')

        elif opcao == 2:
            self.desempilha()

        elif opcao == 3:
            self.desempilha()
            self.empilha('id')
            self.empilha('->')
            self.empilha('leia')

        elif opcao == 4:
            self.desempilha()
            self.empilha('<MESSAGE>')
            self.empilha('->')
            self.empilha('escreva')
        
        elif opcao == 5:
            self.desempilha()
            self.empilha('<IF>')

        elif opcao == 7:
            self.desempilha()
            self.empilha('<WHILE>')
        
        elif opcao == 8:
            self.desempilha()
            self.empilha('id')

        elif opcao == 9:
            self.desempilha()
            self.empilha('string')

        elif opcao == 10:
            self.desempilha()

        elif opcao == 11:
            self.desempilha()
            self.empilha('\n')

        elif opcao == 12:
            self.desempilha()
            self.empilha('<EXPRESSION>')
            self.empilha('=')
            self.empilha('id')

        elif opcao == 13:
            self.desempilha()

        elif opcao == 14:
            self.desempilha()
            self.empilha('<ELSE>')

        elif opcao == 15:
            self.desempilha()
            self.empilha('<IF_ELSE>')
            self.empilha('}')
            self.empilha('<STMT_LIST>')
            self.empilha('{')
            self.empilha(')')
            self.empilha('<COMP>')
            self.empilha('(')
            self.empilha('se')

        elif opcao == 16:
            self.desempilha()
            self.empilha('}')
            self.empilha('<STMT_LIST>')
            self.empilha('{')
            self.empilha('senao')

        elif opcao == 17:
            self.desempilha()
            self.empilha('<TERM_TAIL>')
            self.empilha('<TERM>')
        
        elif opcao == 18:
            self.desempilha()
            self.empilha('<TERM_TAIL>')
            self.empilha('<TERM>')
            self.empilha('<PLUS_MINUS>')

        elif opcao == 19:
            self.desempilha()

        elif opcao == 20:
            self.desempilha()
            self.empilha('<FACTOR_TAIL>')
            self.empilha('<FACTOR>')

        elif opcao == 21:
            self.desempilha()
            self.empilha('<FACTOR_TAIL>')
            self.empilha('<FACTOR>')
            self.empilha('<MULT_OPERATOR>')

        elif opcao == 22:
            self.desempilha()

        elif opcao == 23:
            self.desempilha()
            self.empilha(')')
            self.empilha('<EXPRESSION>')
            self.empilha('(')

        elif opcao == 24:
            self.desempilha()
            self.empilha('id')
        
        # TODO: arrumar no lexico para devolver 'number' ao inves do numero em si
        elif opcao == 25:
            self.desempilha()
            self.empilha('number')

        elif opcao == 26:
            self.desempilha()
            self.empilha('>')

        elif opcao == 27:
            self.desempilha()
            self.empilha('<')

        elif opcao == 28:
            self.desempilha()
            self.empilha('==')

        elif opcao == 29:
            self.desempilha()
            self.empilha('!=')

        elif opcao == 30:
            self.desempilha()
            self.empilha('*')
        
        elif opcao == 31:
            self.desempilha()
            self.empilha('/')

        elif opcao == 32:
            self.desempilha()
            self.empilha('+')

        elif opcao == 33:
            self.desempilha()
            self.empilha('-')

        elif opcao == 34:
            self.desempilha()
            self.empilha('<EXPRESSION>')
            self.empilha('<RELATIONAL_OPERATOR>')
            self.empilha('<EXPRESSION>')

        elif opcao == 35:
            self.desempilha()
            self.empilha('}')
            self.empilha('<STMT_LIST>')
            self.empilha('{')
            self.empilha(')')
            self.empilha('<COMP>')
            self.empilha('(')
            self.empilha('enquanto')

    def peek(self):
        return self.pilha_comandos[0]


    def analisa(self):
        """Analisador Sintatico"""
        print(self.lista_tokens)
        tamanho = len(self.lista_tokens)
        i = 1
        while i < tamanho:
            # self.pilha_comandos.pop()
            saida = open('saida_sintatico.txt', 'w')

            #print("Ultimo elemento: " + str(self.pilha_lexico[0]))
            saida.write(str(self.pilha_comandos))

            if self.peek() == self.lista_tokens[0]:
                self.desempilha()
                del self.lista_tokens[0]
                return "Tudo ok!"
            elif self.lista_tokens[0] == '$' or 'id' or 'leia' or 'escreva' or 'se' or 'enquanto':
                self.procedimento(0)
                print('encontrei: ' + self.lista_tokens[0])
                break
            elif self.peek() == '$' or '}':
                self.procedimento(2)

            elif self.peek() == 'id' or 'leia' or 'escreva' or 'se' or 'senao' or 'enquanto':
                self.procedimento(1)

            elif self.peek() == 'id':
                self.procedimento(6)

            i += 1
            # print(self.pilha_comandos)

        # print(self.lista_tokens)
        # print(self.pilha_comandos)
            


# print(arquivo.readline())
