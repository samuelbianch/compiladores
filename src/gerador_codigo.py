from intermediario import GeradorIntermediario

class GeradorCodigo():
    
    def __init__(self, intermediario, lista_expressoes):
        self.saida = open('../assembly/saida_assembly.asm', 'w')
        self.intermediario = intermediario
        self.cont_string = -1
        self.lista_por_comandos = []
        self.lista_expressoes = lista_expressoes
        print("Aqui fio: ", lista_expressoes)
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
        #print(self.lista_por_comandos)
        i = 0
        contador_expressoes = 0
        while i < len(self.lista_por_comandos):
            if self.lista_por_comandos[i][1] == 'leia':
                self.saida.write(self.leia(self.lista_por_comandos[i+2][1]))
                i += 2

            elif self.lista_por_comandos[i][1] == 'escreva':
                self.saida.write(self.escreva_string())
                i += 1

            elif self.lista_por_comandos[i][1] == 'se':
                i += 2
                ex1 = ""
                ex2 = ""
                ex1 += self.lista_por_comandos[i][1]
                i += 1
                op = self.lista_por_comandos[i][1]
                i += 1
                ex2 += self.lista_por_comandos[i][1]
                i += 1
                self.saida.write(self.condicao(ex1, op, ex2))

            else:
                i += 1
            
    def incrementa_string(self):
        self.cont_string += 1
        return self.cont_string

    def comparacao(self, entrada1, entrada2):
        string = "CMP " + entrada1 + ", " + entrada2
        return string
    
    def menor_que(self, entrada1, entrada2):
        string = "\n\tJL " + entrada1 + ", " + entrada2
        return string
    
    def igual(self, entrada1, entrada2):
        string = "\n\tJE " + entrada1 + ", " + entrada2
        return string

    def diferente(self, entrada1, entrada2):
        string = "\n\tJNE " + entrada1 + ", " + entrada2
        return string
    
    def maior_que(self, entrada1, entrada2):
        string = "\n\tJG " + entrada1 + ", " + entrada2
        return string
    
    def pular_para(self, entrada):
        string = "\n\tJMP " + entrada
        return string
    
    def chamada(self, entrada):
        string = "\n\tCALL " + entrada
        return string
    
    def repeticao(self):
        string = "\n\t.repete\n"
        string += self.condicao()
        return string
    
    def condicao(self, ex1, op, ex2):
        string = ""
        if op == '>':
            string = self.maior_que(ex1, ex2)
        if op == '<':
            string = self.menor_que(ex1, ex2)
        if op == '==':
            string = self.igual(ex1, ex2)
        if op == '!=':
            string = self.diferente(ex1, ex2)

        return string
        
    def leia(self, entrada):
        string = "\n\n\tPUSH " + entrada +"; lendo uma entrada\n\tPUSH in_out\n\tCALL scanf"
        return string

    def escreva_string(self):
        string = "\n\n\tPUSH string" + str(self.incrementa_string()) + "; escrevendo string em tela\n\tCALL printf"
        return string
