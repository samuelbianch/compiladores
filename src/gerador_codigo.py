from intermediario import GeradorIntermediario
from lexico import AnalisadorLexico
from typing import List

class GeradorCodigo():
    
    def __init__(self, intermediario, lista_expressoes, lista_strings):
        self.saida = open('D:\\apps\compiladores\\assembly\saida_assembly.asm', 'w')
        self.intermediario = intermediario
        self.cont_string = -1
        self.contador_labels = -1
        self.lista_por_comandos = []
        self.lista_expressoes = lista_expressoes
        self.listaStrings = lista_strings
        self.labels = ""
        self.posso_escrever = True
        self.lista = []
        self.guarda_label_enquanto = 0
        self.lista_variaveis = AnalisadorLexico.get_lista_variaveis_to_intermediario()
        #print("Aqui fio: ", lista_expressoes)
        with open('D:\\apps\compiladores\out\saida_lexico.txt', 'r') as arquivo:
            self.lista_lexica = arquivo.readlines()
            arquivo.close()

    def elemento_lista(self):
        if len(self.lista) > 0:
            aux = self.lista[0]
            self.lista.remove(aux)
            return aux
        
    def recebe_label(self):
        i = 0
        #label = self.cont_labels()
        
        while i < len(self.lista):
            j = 0
            aux = self.lista[i].split()
            for c in aux:
                if aux[j].isupper():
                    aux[j] = '\n\t' + aux[j]
                if c == 'label_':
                    x = ' '.join(aux)
                    self.lista[i] = x + str(self.contador_labels+1)
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
        self.guarda_label_enquanto = 0
        enquanto = False
        while i < len(self.lista_por_comandos):
            
            #if self.lista_por_comandos[i][1] == '}' and self.lista_por_comandos[i+1][1] == ';':
            #    if not self.lista:
             #       self.saida.write("\n\tJMP label_" + str(self.guarda_label_enquanto))

            if self.lista_por_comandos[i][1] == '}':
                #self.lista.append("\n\tJMP label_" + str(self.guarda_label_enquanto))
                while len(self.lista) > 0:
                    self.recebe_label()
                    self.saida.write(self.elemento_lista())
                    if len(self.lista) == 0:
                        if posso_terminar and enquanto == False:
                            self.saida.write("\n\tRET")
                        if enquanto:
                            self.saida.write("\n\tJMP label_" + str(self.guarda_label_enquanto))
                            enquanto = False
                        #self.saida.write("\n\nlabel_" + str(label+1) + ":")
                
            elif self.lista_por_comandos[i][1] == 'leia':
                if not len(self.lista) > 0:
                    self.saida.write(self.leia(self.lista_por_comandos[i+2][1]))
                else:
                    self.lista.append(self.leia(self.lista_por_comandos[i+2][1]))

            elif self.lista_por_comandos[i][1] == 'escreva':
                string = self.lista_por_comandos[i+2][1]
                if not len(self.lista) > 0:
                    self.saida.write(self.escreva_string(string))
                else:
                    self.lista.append(self.escreva_string(string))

                posso_terminar = True

            elif self.lista_por_comandos[i][1] == '{':
                label = self.cont_labels()
                self.saida.write("\n\nlabel_" + str(self.contador_labels) +":")


            elif self.lista_por_comandos[i][1] == '=':
                variavel = self.lista_por_comandos[i-1][1]
                i += 1
                expressao = ""
                while self.lista_por_comandos[i][1] != ';':
                    expressao += " " + self.lista_por_comandos[i][1]
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
                self.lista.append("\n\nlabel_" + str(self.cont_labels()) + ":")

            elif self.lista_por_comandos[i][1] == 'enquanto':
                enquanto = True
                #self.saida.write('\n\nlabel_' + str(self.contador_labels+1) + ":\n\t;enquanto")
                self.guarda_label_enquanto = label
                i += 2
                ex1 = ""
                ex2 = ""
                ex1 += self.lista_por_comandos[i][1]
                i += 1
                op = self.lista_por_comandos[i][1]
                i += 1
                ex2 += self.lista_por_comandos[i][1]

                self.lista.append(self.condicao(ex1, op, ex2, label+contador))
                
            
            print("lista por comando: ", self.lista_por_comandos[i][1])
            i += 1
        self.saida.write("\n\nlabel_" + str(self.contador_labels+1) +":\n\tRET")
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
        

    def escreva_string(self, string):
        if string not in self.lista_variaveis:    
            return "\n\n\tPUSH string" + str(self.incrementa_string()) + "; escrevendo string em tela\n\tCALL printf"
        else:
            return"\n\n\tMOV eax, [" + string + "]\n\tPUSH eax \n\tPUSH in_out; escrevendo string em tela\n\tCALL printf"

    def recebe(self, expressao, variavel):
        expressao_posfixa = GeradorIntermediario.infixToPostfix(expressao)
        print("Expressao posfixa", expressao_posfixa.split())
        
        string = ""
        i = 0
        expressao_posfixa = expressao_posfixa.split()

        if len(expressao_posfixa) == 1:
            if expressao_posfixa[0].isnumeric():
                return "\n\tMOV eax, " + str(expressao_posfixa[0]) + "; recebendo um numero inteiro\n\tMOV [" + variavel + "], eax" 
        Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
        pilha = []

        for c in expressao_posfixa:
            if c not in Priority:
                pilha.append(c)
            else:
                val1 = pilha.pop()
                val2 = pilha.pop()
                if val1 in self.lista_variaveis:
                    val1 = "[" + val1 + "]"
                if val2 in self.lista_variaveis:
                    val2 = "[" + val2 + "]" 
                string += "\n\tMOV eax, " + val1 + "\n\tMOV ebx, " + val2
                if c == '+':
                    string += self.soma()
                elif c == '-':
                    string += self.sub()
                elif c == '/':
                    string += self.div()
                elif c == '*':
                    string += self.mult()
        return string + "\n\tMOV [" + variavel + "], eax"
    
    def mov_registradores(self, a, b):
        if a in self.lista_variaveis:
            a = "[" + a + "]"
        if b in self.lista_variaveis:
            b = "[" + b + "]"
        return "\n\n\tMOV ebx, " + a + "\n\tMOV ecx, " + b
    
    def soma(self):
        return "\n\tADD eax, ebx ; somando dois inteiros"
    
    def sub(self):
        return "\n\tSUB eax, ebx ; subtraindo dois inteiros"
    
    def div(self):
        return "\n\tDIV eax ; dividindo dois inteiros"
    
    def mult(self):
        return "\n\tIMUL eax, ebx ; multiplicando dois inteiros"