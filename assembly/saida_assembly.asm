section .data ; declara constantes
   string0: DB 'Equilatero', 10, 0
   string1: DB 'Isoceles', 10, 0
   string2: DB 'Isoceles', 10, 0
   string3: DB 'Escaleno', 10, 0
   string4: DB 'ERRO', 10, 0


section .bss ; declara as variaveis
   a: RESD 1
   b: RESD 1
   c: RESD 1


section .text ; importa scanf e printf do gcc compiler
   global _main
   extern _printf
   extern _scanf