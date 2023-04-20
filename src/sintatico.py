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
        if len(self.pilha_comandos) > 0:
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

        elif opcao == 6:
            self.desempilha()
            self.empilha('<GET>')

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
        return self.pilha_comandos[len(self.pilha_comandos)-1]


    def analisa(self):
        """Analisador Sintatico"""
        # print(self.lista_tokens)
        tamanho = len(self.lista_tokens)
        i = 1

        # Cria o arquivo de saída
        saida = open('../out/saida_sintatico.txt', 'w')
        #print("Topo da pilha: " + self.peek())
        while len(self.lista_tokens) > 0:
            # self.pilha_comandos.pop()
            

            #print("Ultimo elemento: " + str(self.pilha_lexico[0]))
            saida.write(str(self.pilha_comandos) + "\n")
            #print("ENTREI AQUI")
            if self.peek() == self.lista_tokens[0][0]:
                self.desempilha()
                del self.lista_tokens[0]

            # Caso o topo da pilha for <PROGRAM>
            elif self.peek() == '<PROGRAM>':
                lista_temp = ['$', 'id', 'leia', 'escreva', 'se', 'enquanto']
                if self.lista_tokens[0][0] in lista_temp:
                    self.procedimento(0)
                else:
                    print("ERRO! Esperava-se uma palavra reservada, mas foi encontrado: " + self.lista_tokens[0][0] + " - Linha: ", self.lista_tokens[0][1], ", Coluna: ", self.lista_tokens[0][2])
                    exit(0)

            # Caso o topo da pilha seja <STMT_LIST>
            elif self.peek() == '<STMT_LIST>':
                # print(self.lista_tokens[0][0])
                lista_temp = ['$', '}']
                lista_temp2 = ['id', 'leia', 'escreva', 'se', 'enquanto']

                if self.lista_tokens[0][0] in lista_temp:
                    self.procedimento(2)

                elif self.lista_tokens[0][0] in lista_temp2:
                    self.procedimento(1)

                else:
                    print("ERRO! Esperava-se uma palavra reservada, mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso o topo da pilha seja <STMT>
            elif self.peek() == '<STMT>':
                if self.lista_tokens[0][0] == 'id':
                    self.procedimento(6)

                elif self.lista_tokens[0][0] == 'leia':
                    self.procedimento(3)

                elif self.lista_tokens[0][0] == 'escreva':
                    self.procedimento(4)
                
                elif self.lista_tokens[0][0] == 'se':
                    self.procedimento(5)

                elif self.lista_tokens[0][0] == 'enquanto':
                    self.procedimento(7)

                else:
                    print("ERRO! Esperava-se uma palavra reservada, mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <GET>
            elif self.peek() == '<GET>':
                if self.lista_tokens[0][0] == 'id':
                    self.procedimento(12)

                else:
                    print("ERRO! Esperava-se um ID, mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <EXPRESSION>
            elif self.peek() == '<EXPRESSION>':
                lista_temp = ['(', 'number', 'id']
                if self.lista_tokens[0][0] in lista_temp:
                    self.procedimento(17)

                else:
                    print("ERRO! Esperava-se uma [(, number, id], mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <RELATIONAL_OPERATOR>
            elif self.peek() == '<RELATIONAL_OPERATOR>':
                if self.lista_tokens[0][0] == '>':
                    self.procedimento(26)

                elif self.lista_tokens[0][0] == '<':
                    self.procedimento(27)

                
                elif self.lista_tokens[0][0] == '==':
                    self.procedimento(28)

                elif self.lista_tokens[0][0] == '!=':
                    self.procedimento(29)

                else:
                    print("ERRO! Esperava-se um operador relacional, mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <MESSAGE>
            elif self.peek() == '<MESSAGE>':
                if self.lista_tokens[0][0] == ';':
                    self.procedimento(10)

                elif self.lista_tokens[0][0] == '\n':
                    self.procedimento(11)

                elif self.lista_tokens[0][0] == 'id':
                    self.procedimento(8)

                elif self.lista_tokens[0][0] == 'string':
                    self.procedimento(9)

                else:
                    print("ERRO! Esperava-se uma palavra reservada, mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <PLUS_MINUS>
            elif self.peek() == '<PLUS_MINUS>':
                if self.lista_tokens[0][0] == '+':
                    self.procedimento(32)

                elif self.lista_tokens[0][0] == '-':
                    self.procedimento(33)

                else:
                    print("ERRO! Esperava-se um sinal de mais ou menos, mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <TERM>
            elif self.peek() == '<TERM>':
                lista_temp = ['(', 'id', 'number']
                if self.lista_tokens[0][0] in lista_temp:
                    self.procedimento(20)
                
                else:
                    print("ERRO! Esperava-se [(, id, number], mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <MULT_OPERATOR>
            elif self.peek() == '<MULT_OPERATOR>':
                if self.lista_tokens[0][0] == '*':
                    self.procedimento(30)

                elif self.lista_tokens[0][0] == '/':
                    self.procedimento(31)

                else:
                    print("ERRO! Esperava-se uma o sinal de multiplicação ou divisão, mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <IF_ELSE>
            elif self.peek() == '<IF_ELSE>':
                if self.lista_tokens[0][0] == ';':
                    self.procedimento(13)

                elif self.lista_tokens[0][0] == 'senao':
                    self.procedimento(14)

                else:
                    print("ERRO! Esperava-se o ';' ou o 'senao', mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <IF>
            elif self.peek() == '<IF>':
                if self.lista_tokens[0][0] == 'se':
                    self.procedimento(15)

                else:
                    print("ERRO! Esperava-se o operador 'se', mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <ELSE>
            elif self.peek() == '<ELSE>':           
                if self.lista_tokens[0][0] == 'senao':
                    self.procedimento(16)

                else:
                    print("ERRO! Esperava-se o operador 'senao', mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <FACTOR>
            elif self.peek() == '<FACTOR>':
                if self.lista_tokens[0][0] == '(':
                    self.procedimento(23)

                elif self.lista_tokens[0][0] == 'number':
                    self.procedimento(25)

                elif self.lista_tokens[0][0] == 'id':
                    self.procedimento(24)

                else:
                    print("ERRO! Esperava-se [(, number, id], mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <TERM_TAIL>
            elif self.peek() == '<TERM_TAIL>':
                lista_temp = [';', ')', '>', '<', '==', '!=']
                lista_temp2 = ['+', '-']
                if self.lista_tokens[0][0] in lista_temp:
                    self.procedimento(19)

                elif self.lista_tokens[0][0] in lista_temp2:
                    self.procedimento(18)

                else:
                    print("ERRO! Esperava-se operadores, mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

             # Caso topo da pilha seja <FACTOR_TAIL>
            elif self.peek() == '<FACTOR_TAIL>':
                lista_temp = [';', ')', '>', '<', '!=', '+', '-', '==']
                lista_temp2 = ['*', '/']
                if self.lista_tokens[0][0] in lista_temp:
                    self.procedimento(22)

                elif self.lista_tokens[0][0] in lista_temp2:
                    self.procedimento(21)

                else:
                    print("ERRO! Esperava-se operadores, mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <COMP>
            elif self.peek() == '<COMP>':
                lista_temp = ['(', 'number', 'id']
                if self.lista_tokens[0][0] in lista_temp:
                    self.procedimento(34)

                else:
                    print("ERRO! Esperava-se [(, number, id], mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)

            # Caso topo da pilha seja <WHILE>
            elif self.peek() == '<WHILE>':
                if self.lista_tokens[0][0] == 'enquanto':
                    self.procedimento(35)

                else:
                    print("ERRO! Esperava-se a palavra enquanto, mas foi encontrado: " + self.lista_tokens[0][0])
                    exit(0)
            i += 1

            #if self.lista_tokens:
                #print("Laço: "+ str(i) + " Pilha: " + str(self.pilha_comandos))
                #print("Laço: " + str(i) + " Lista: " + str(self.lista_tokens[0][0]))


# print(arquivo.readline())
