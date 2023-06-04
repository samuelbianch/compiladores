from intermediario import GeradorIntermediario
from lexico import AnalisadorLexico
from typing import List

class GeradorCodigo():
    
    def __init__(self, intermediario, lista_expressoes, lista_strings):
        self.saida = open('../assembly/saida_assembly.asm', 'w')
        self.intermediario = intermediario
        self.cont_string = -1
        self.contador_labels = -1
        self.lista_por_comandos = []
        self.lista_expressoes = lista_expressoes
        self.listaStrings = lista_strings
        self.labels = ""
        self.posso_escrever = True
        self.pilha: List[str] = []
        self.lista_variaveis = AnalisadorLexico.get_lista_variaveis_to_intermediario()
        #print("Aqui fio: ", lista_expressoes)
        with open('../out/saida_lexico.txt', 'r') as arquivo:
            self.lista_lexica = arquivo.readlines()
            arquivo.close()

    def empilha(self, elemento):
        self.pilha.append(elemento)

    def peek(self):
        return self.pilha[len(self.pilha)-1]

    def desempilha(self):
        while len(self.pilha) > 0:
            print("Topo da pilha: ", self.peek())
            self.saida.write(self.peek())
            self.pilha.pop()

    def vazia(self):
        if len(self.pilha) > 0:
            return False
        return True

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
        jump = 0
        contador_de_abertura = 0
        while i < len(self.lista_por_comandos):
            
            if self.lista_por_comandos[i][1] == 'leia':
                if self.vazia():
                    self.saida.write(self.leia(self.lista_por_comandos[i+2][1]))
                else:
                    self.empilha(self.leia(self.lista_por_comandos[i+2][1]))

            elif self.lista_por_comandos[i][1] == 'escreva':
                if self.vazia():
                    self.saida.write(self.escreva_string())
                else:
                    self.empilha(self.escreva_string())

            elif self.lista_por_comandos[i][1] == '{':
                contador_de_abertura += 1
                label = self.cont_labels()
                self.saida.write("\n\tJMP label_" + str(label+contador_de_abertura))
                self.saida.write("\n\nlabel_" + str(label) + ":")

            elif self.lista_por_comandos[i][1] == '}' and self.lista_por_comandos[i+1][1] == ';':
                jump += 1
                #self.empilha("\n\tRET")
                self.desempilha()
                contador_de_abertura = 0
                self.posso_escrever = True
                

            elif self.lista_por_comandos[i][1] == '=':
                variavel = self.lista_por_comandos[i-1][1]
                i += 1
                expressao = 0
                while self.lista_por_comandos[i][1] != ';':
                    expressao = self.lista_por_comandos[i][1]
                if self.vazia():
                    self.saida.write(self.recebe(expressao, variavel))
                else:
                    self.empilha(self.recebe(expressao, variavel))
            
            elif self.lista_por_comandos[i][1] == 'se':
                i += 2
                ex1 = ""
                ex2 = ""
                ex1 += self.lista_por_comandos[i][1]
                i += 1
                op = self.lista_por_comandos[i][1]
                i += 1
                ex2 += self.lista_por_comandos[i][1]
                if self.vazia():
                    self.saida.write(self.condicao(ex1, op, ex2, label))
                    #self.saida.write("\n\tJMP label_" + str(label))
                             
                else:
                    self.empilha("\n\nlabel_" + str(jump) + ":")
                    self.empilha(self.condicao(ex1, op, ex2, label))
                    #self.empilha("\n\tJMP label_" + str(label))
                    self.posso_escrever = False
                #self.posso_escrever = True
            
            print("lista por comando: ", self.lista_por_comandos[i][1])
            i += 1
            
            
    def incrementa_string(self):
        self.cont_string += 1
        return self.cont_string

    def comparacao(self, entrada1, entrada2):
        if entrada1 in self.lista_variaveis:
            entrada1 = '[' + entrada1 + ']'
        if entrada2 in self.lista_variaveis:
            entrada2 = '[' + entrada2 + ']'
        string = "\n\n\tMOV ebx, " + entrada1 + "\n\tMOV ecx, " + entrada2
        return string + "\n\tCMP ebx, ecx"
    
    def menor_que(self, n):
        return "\n\tJL label_" + str(n) 
    
    def igual(self, n):
        return "\n\tJE label_" + str(n)

    def diferente(self, n):
        return "\n\tJNE label_" + str(n)
    
    def maior_que(self, n):
        return "\n\tJG label_" + str(n)
    
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
        if op == '>':
            string += self.maior_que(n)
        if op == '<':
            string += self.menor_que(n)
        if op == '==':
            string += self.igual(n)
        if op == '!=':
            string += self.diferente(n)

        return string
        
    def leia(self, entrada):
        return "\n\n\tPUSH " + entrada +"; lendo uma entrada\n\tPUSH in_out\n\tCALL scanf"
        

    def escreva_string(self):
        return "\n\n\tPUSH string" + str(self.incrementa_string()) + "; escrevendo string em tela\n\tCALL printf"
        

    def recebe(self, expressao, variavel):
        if expressao in self.lista_variaveis:
            expressao = "[" + expressao + "]"
        return "\n\n\tMOV eax, " + expressao + "\n\tMOV [" + variavel + "], eax"