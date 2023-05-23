from intermediario import GeradorIntermediario

class GeradorCodigo():
    
    def __init__(self, intermediario):
        self.saida = open('../assembly/saida_assembly.asm', 'w')
        self.intermediario = intermediario


    def main(self):
        self.saida.write(self.intermediario)
        