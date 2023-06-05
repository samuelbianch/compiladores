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
   x: RESD 1


section .text ; importa scanf e printf do gcc compiler
	global main
	extern printf
	extern scanf

main:


	PUSH linhastotal; lendo uma entrada
	PUSH in_out
	CALL scanf

	MOV eax, 0
	MOV [linhaatual], eax

	MOV eax, 0
	MOV [colunaatual], eax

	MOV eax, 1
	MOV [fatorialn], eax

	MOV eax, 1
	MOV [fatorialp], eax

	MOV eax, 1
	MOV [fatorialx], eax

	MOV ebx, [linhastotal]
	MOV ecx, 1
	CMP ebx, ecx
	JG label_0
	JMP label_1

label_0:

	MOV eax, 0
	MOV [colunaatual], eax

	MOV eax, 1
	MOV [fatorialn], eax

	MOV eax, 1
	MOV [fatorialp], eax

	MOV eax, 1
	MOV [fatorialx], eax

	MOV eax, 6
	MOV [x], eax

label_0:
	JMP label_3

label_1:

	MOV eax, 1
	MOV [fatorialn], eax

	MOV eax, 1
	MOV [fatorialp], eax

	MOV eax, 1
	MOV [fatorialx], eax

	MOV eax, [linhaatual]
	MOV [n], eax

label_0:
	JMP label_5

label_2:

	MOV eax, [n]
	MOV [fatorialn], eax

	MOV eax, 1
	MOV [n], eax

	MOV eax, [colunaatual]
	MOV [p], eax

label_0:
	JMP label_7

label_3:

	MOV eax, [p]
	MOV [fatorialp], eax

	MOV eax, 1
	MOV [p], eax

	MOV eax, [colunaatual]
	MOV [aux], eax

label_0:
	JMP label_9

label_4:

	MOV eax, [aux]
	MOV [fatorialx], eax

	MOV eax, 1
	MOV [aux], eax

	MOV eax, [fatorialx]
	MOV [denominador], eax

	MOV eax, [denominador]
	MOV [resultado], eax

	PUSH string0; escrevendo string em tela
	CALL printf

	MOV eax, 1
	MOV [colunaatual], eax

	PUSH string1; escrevendo string em tela
	CALL printf

	MOV eax, 1
	MOV [linhaatual], eax

	MOV eax, 1
	MOV [x], eax

label_0:
	JMP label_11

label_5:

	PUSH string2; escrevendo string em tela
	CALL printf