from intermediario import GeradorIntermediario
from lexico import AnalisadorLexico
from typing import List

class GeradorCodigo():
    
    def __init__(self, intermediario, lista_expressoes, lista_strings):
        self.saida = open('D:\Programação\compiladores\\assembly\saida_assembly.asm', 'w')
        self.intermediario = intermediario
        self.cont_string = -1
        self.contador_labels = -1
        self.lista_por_comandos = []
        self.lista_expressoes = lista_expressoes
        self.listaStrings = lista_strings
        self.labels = ""
        self.posso_escrever = True
        self.lista = []
        self.lista_variaveis = AnalisadorLexico.get_lista_variaveis_to_intermediario()
        #print("Aqui fio: ", lista_expressoes)
        with open('D:\Programação\compiladores\out\saida_lexico.txt', 'r') as arquivo:
            self.lista_lexica = arquivo.readlines()
            arquivo.close()

    def elemento_lista(self):
        if len(self.lista) > 0:
            aux = self.lista[0]
            self.lista.remove(aux)
            return aux
        
    def recebe_label(self):
        i = 0
        label = self.cont_labels()
        
        while i < len(self.lista):
            j = 0
            aux = self.lista[i].split()
            for c in aux:
                if aux[j].isupper():
                    aux[j] = '\n\t' + aux[j]
                if c == 'label_':
                    x = ' '.join(aux)
                    self.lista[i] = x + str(label)
                j += 1
            i += 1

    def cont_labels(self):
        self.contador_labels += 1
        return self.contador_labels
    
    def main(self):
        self.saida.write(self.intermediario)
        self.saida.write("\n\nmain:\n")
        i = 0
        while i < len(self.lista_lexica):
            comando = self.lista_lexica[i].split(',')
            self.lista_por_comandos.append(comando)
            i += 1
        print(self.lista_por_comandos)
        i = 0
        self.posso_escrever = True
        label = 0
        posso_terminar = False
        contador = 0
        while i < len(self.lista_por_comandos):
            
            if self.lista_por_comandos[i][1] == '}':
                while len(self.lista) > 0:
                    self.recebe_label()
                    self.saida.write(self.elemento_lista())
                    if len(self.lista) == 0:
                        if posso_terminar:
                            self.saida.write("\n\tRET")
                        self.saida.write("\n\nlabel_" + str(label+1) + ":")
                

            elif self.lista_por_comandos[i][1] == 'leia':
                if not len(self.lista) > 0:
                    self.saida.write(self.leia(self.lista_por_comandos[i+2][1]))
                else:
                    self.lista.append(self.leia(self.lista_por_comandos[i+2][1]))

            elif self.lista_por_comandos[i][1] == 'escreva':
                if not len(self.lista) > 0:
                    self.saida.write(self.escreva_string())
                else:
                    self.lista.append(self.escreva_string())

                posso_terminar = True

            elif self.lista_por_comandos[i][1] == '{':
                label = self.cont_labels()
                posso_terminar = False

            elif self.lista_por_comandos[i][1] == '=':
                variavel = self.lista_por_comandos[i-1][1]
                i += 1
                expressao = ""
                while self.lista_por_comandos[i][1] != ';':
                    expressao += self.lista_por_comandos[i][1]
                    i += 1
                expressao = expressao.strip()
                if not len(self.lista) > 0:
                    self.saida.write(self.recebe(expressao, variavel))
                else:
                    self.lista.append(self.recebe(expressao, variavel))
            
            elif self.lista_por_comandos[i][1] == 'se':
                contador += 1
                i += 2
                ex1 = ""
                ex2 = ""
                ex1 += self.lista_por_comandos[i][1]
                i += 1
                op = self.lista_por_comandos[i][1]
                i += 1
                ex2 += self.lista_por_comandos[i][1]
                if (label + 2) % 2 == 0:
                    self.lista.append(self.condicao(ex1, op, ex2, label+contador))
                else:
                    self.lista.append(self.condicao(ex1, op, ex2, label+contador+1))

            elif self.lista_por_comandos[i][1] == 'senao':
                #self.lista.append("\n\tRET")
                self.lista.append("\n\nlabel_" + str(self.contador_labels) + ":")

            elif self.lista_por_comandos[i][1] == 'enquanto':
                self.saida.write('\n\nlabel_' + str(label) + ':')
                i += 2
                ex1 = ""
                ex2 = ""
                ex1 += self.lista_por_comandos[i][1]
                i += 1
                op = self.lista_por_comandos[i][1]
                i += 1
                ex2 += self.lista_por_comandos[i][1]
            
            print("lista por comando: ", self.lista_por_comandos[i][1])
            i += 1
        print("Expressoes: ", self.lista_expressoes)
            
            
    def incrementa_string(self):
        self.cont_string += 1
        return self.cont_string

    def comparacao(self, entrada1, entrada2):
        if entrada1 in self.lista_variaveis:
            entrada1 = '[' + entrada1 + ']'
        if entrada2 in self.lista_variaveis:
            entrada2 = '[' + entrada2 + ']'
        string = "\n\n\tMOV ebx, " + entrada1 + " ; inicia uma comparacao\n\tMOV ecx, " + entrada2
        return string + "\n\tCMP ebx, ecx"
    
    def menor_que(self, n):
        return "\n\tJL label_"
    
    def igual(self, n):
        return "\n\tJE label_"

    def diferente(self, n):
        return "\n\tJNE label_"
    
    def maior_que(self, n):
        return "\n\tJG label_"
    
    def pular_para(self, entrada):
        return "\n\tJMP label_" + entrada
    
    def chamada(self, entrada):
        return "\n\tCALL " + entrada
    
    def repeticao(self):
        string = "\n\t.repete\n"
        string += self.condicao()
        return string
    
    def condicao(self, ex1, op, ex2, n):
        string = self.comparacao(ex1, ex2)
        if op == '<':
            string += self.maior_que(n)
        if op == '>':
            string += self.menor_que(n)
        if op == '!=':#jne
            string += self.igual(n)
        if op == '==':#je
            string += self.diferente(n)

        return string
        
    def leia(self, entrada):
        return "\n\n\tPUSH " + entrada +"; lendo uma entrada\n\tPUSH in_out\n\tCALL scanf"
        

    def escreva_string(self):
        return "\n\n\tPUSH string" + str(self.incrementa_string()) + "; escrevendo string em tela\n\tCALL printf"
        

    def recebe(self, expressao, variavel):
        expressao_posfixa = GeradorIntermediario.infixToPostfix(expressao)
        print(expressao_posfixa)
        string = ""
        operadores = ['+', '-', '*', '/']
        i = 0
        for c in expressao_posfixa:
            if c in operadores:
                while i < len(expressao_posfixa):
                    if expressao_posfixa[i] not in operadores:
                        string += "\n\n\tMOV ebx, [" + expressao_posfixa[i] + "] ; iniciando uma operacao aritmetica"
                        i += 1
                    if expressao_posfixa[i] not in operadores:
                        string += "\n\tMOV ecx, [" + expressao_posfixa[i] + "]"
                        i += 1
                    if expressao_posfixa[i] in operadores:
                        if expressao_posfixa[i] == '+':
                            string += self.soma()
                        if expressao_posfixa[i] == '-':
                            string += self.sub()
                        if expressao_posfixa[i] == '/':
                            string += self.div()
                        if expressao_posfixa[i] == '*':
                            string += self.mult()
                        
                    i += 1
        if expressao_posfixa.isnumeric():
            return "\n\tMOV eax, " + str(expressao_posfixa) + "; recebendo um numero inteiro\n\tMOV [" + variavel + "], eax" 
        return string + "\n\tMOV [" + variavel + "], ebx ; recebe um valor apos a operacao"
    
    def mov_registradores(self, a, b):
        if a in self.lista_variaveis:
            a = "[" + a + "]"
        if b in self.lista_variaveis:
            b = "[" + b + "]"
        return "\n\n\tMOV ebx, " + a + "\n\tMOV ecx, " + b
    
    def soma(self):
        return "\n\tADD ebx, ecx"
    
    def sub(self):
        return "\n\tSUB ebx, ecx"
    
    def div(self):
        return "\n\tDIV ebx, ecx"
    
    def mult(self):
        return "\n\tMUL ebx, ecx"