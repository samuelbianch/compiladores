class GeradorCodigo():
    
    def __init__(self):
        self.saida = open('../out/saida_assembly.asm', 'w')

    def get_esqueleto(self):
        return 'section .data\n\nsection .bss\n\nsection.text\n   global _main\n   extern _printf\n   extern _scanf\n\n_main:'

    def main(self):
        self.saida.write(self.get_esqueleto())
        