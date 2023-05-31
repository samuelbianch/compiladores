from intermediario import GeradorIntermediario

class GeradorCodigo():
    
    def __init__(self, intermediario, lista_expressoes):
        self.saida = open('../assembly/saida_assembly.asm', 'w')
        self.intermediario = intermediario
        self.cont_string = -1
        self.lista_por_comandos = []
        self.lista_expressoes = lista_expressoes
        with open('../out/saida_lexico.txt', 'r') as arquivo:
            self.lista_lexica = arquivo.readlines()
            arquivo.close()

        


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
        contador_expressoes = 0
        while i < len(self.lista_por_comandos):
            if self.lista_por_comandos[i][1] == 'leia':
                self.saida.write(self.leia(self.lista_por_comandos[i+2][1]))
                i += 2

            elif self.lista_por_comandos[i][1] == 'escreva':
                self.saida.write(self.escreva_string())
                i += 1

            else:
                i += 1
            '''if self.lista_por_comandos[i][1] == 'se':
                op = ['==', '!=', '>', '<']
                if op in self.lista_expressoes[contador_expressoes]:

                    self.saida.write(self.condicao(op))'''
            
            


            
                

    def incrementa_string(self):
        self.cont_string += 1
        return self.cont_string

    def comparacao(self, entrada1, entrada2):
        string = "CMP " + entrada1 + ", " + entrada2
        return string
    
    def menor_que(self, entrada1, entrada2):
        string = "JL" + entrada1 + ", " + entrada2
        return string
    
    def igual(self, entrada1, entrada2):
        string = "JE" + entrada1 + ", " + entrada2
        return string

    def diferente(self, entrada1, entrada2):
        string = "JNE" + entrada1 + ", " + entrada2
        return string
    
    def maior_que(self, entrada1, entrada2):
        string = "JG" + entrada1 + ", " + entrada2
        return string
    
    def pular_para(self, entrada):
        string = "JMP" + entrada
        return string
    
    def chamada(self, entrada):
        string = "CALL" + entrada
        return string
    
    def repeticao(self):
        string = ".repete\n"
        string += self.condicao()
        return string
    
    def condicao(self, ex1, op, ex2):
        if op == '>':
            self.maior_que(ex1, ex2)
        if op == '<':
            self.menor_que(ex1, ex2)
        if op == '==':
            self.igual(ex1, ex2)
        if op == '!=':
            self.diferente(ex1, ex2)
        
    def leia(self, entrada):
        string = "\n\n\tPUSH " + entrada +"; lendo uma entrada\n\tPUSH in_out\n\tCALL scanf"
        return string

    def escreva_string(self):
        string = "\n\n\tPUSH string" + str(self.incrementa_string()) + "; escrevendo string em tela\n\tCALL printf"
        return string
