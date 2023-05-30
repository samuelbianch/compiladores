from intermediario import GeradorIntermediario

class GeradorCodigo():
    
    def __init__(self, intermediario):
        self.saida = open('../assembly/saida_assembly.asm', 'w')
        self.intermediario = intermediario
        with open('../out/saida_lexico.txt', 'r') as arquivo:
            self.arquivo = arquivo
            #arquivo.close()


    def main(self):
        self.saida.write(self.intermediario)
        linha = self.arquivo.readline()
        print(linha)

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
    
    def condicao(self,entrada):
        if entrada == '>':
            self.maior_que()
        if entrada == '<':
            self.menor_que()
        if entrada == '==':
            self.igual()
        if entrada == '!=':
            self.diferente()
        
