section .data ; declara constantes
	in_out DB "%d", 0x0
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
	global main
	extern printf
	extern scanf

main:
	PUSH linhastotal
	PUSH in_out
	CALL scanf
	MOV eax, [0]
	PUSH eax
	PUSH in_out
	CALL printf
	MOV eax, [1]
	PUSH eax
	PUSH in_out
	CALL printf
	MOV eax, [2]
	PUSH eax
	PUSH in_out
	CALL printf