section .data ; declara constantes
   string0: DB 'ERRO', 10, 0


section .bss ; declara as variaveis
   aux: RESD 1
   colunaatual: RESD 1
   denominador: RESD 1
   fatorialn: RESD 1
   fatorialp: RESD 1
   fatorialx: RESD 1
   linhaatual: RESD 1
   linhastotal: RESD 1
   n: RESD 1
   p: RESD 1
   resultado: RESD 1


section .text ; importa scanf e printf do gcc compiler
   global _main
   extern _printf
   extern _scanf

_main:
   MOV eax, 10
