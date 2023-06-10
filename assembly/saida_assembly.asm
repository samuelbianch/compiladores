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
	MOV eax, 0; recebendo um numero inteiro
	MOV [linhaatual], eax
	MOV eax, 0; recebendo um numero inteiro
	MOV [colunaatual], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialn], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialp], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialx], eax

label_0:

label_1:

	MOV ebx, [linhaatual] ; inicia uma comparacao
	MOV ecx, [linhastotal]
	CMP ebx, ecx
	JG label_1

label_2:

label_3:

	MOV ebx, [colunaatual] ; inicia uma comparacao
	MOV ecx, [x]
	CMP ebx, ecx
	JG label_3

label_4:

label_5:

	MOV ebx, [n] ; inicia uma comparacao
	MOV ecx, 0
	CMP ebx, ecx
	JL label_5

label_6:

	MOV ebx, [n] ; inicia uma comparacao
	MOV ecx, 0
	CMP ebx, ecx
	JL label_5
	JMP label_8
	MOV ebx, [linhastotal] ; inicia uma comparacao 
	MOV ecx, 0 
	CMP ebx, ecx 
	JL label_7
	MOV eax, 0; recebendo um numero inteiro
	MOV [colunaatual], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialn], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialp], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialx], eax
	MOV eax, 1
	MOV ebx, [linhaatual]
	ADD eax, ebx ; somando dois inteiros
	MOV [x], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialn], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialp], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialx], eax
	MOV [n], eax
	MOV eax, [n]
	MOV ebx, [fatorialn]
	IMUL eax, ebx ; multiplicando dois inteiros
	MOV [fatorialn], eax
	MOV eax, 1
	MOV ebx, [n]
	SUB eax, ebx ; subtraindo dois inteiros
	MOV [n], eax
	JMP label_0
	MOV [p], eax

label_7:

	MOV ebx, [p] ; inicia uma comparacao
	MOV ecx, 0
	CMP ebx, ecx
	JL label_7

label_8:
	MOV eax, [p]
	MOV ebx, [fatorialp]
	IMUL eax, ebx ; multiplicando dois inteiros
	MOV [fatorialp], eax
	MOV eax, 1
	MOV ebx, [p]
	SUB eax, ebx ; subtraindo dois inteiros
	MOV [p], eax

	MOV ebx, [p] ; inicia uma comparacao
	MOV ecx, 0
	CMP ebx, ecx
	JL label_7
	JMP label_10
	MOV eax, [colunaatual]
	MOV ebx, [linhaatual]
	SUB eax, ebx ; subtraindo dois inteiros
	MOV [aux], eax

label_9:

	MOV ebx, [aux] ; inicia uma comparacao
	MOV ecx, 0
	CMP ebx, ecx
	JL label_9

label_10:
	MOV eax, [aux]
	MOV ebx, [fatorialx]
	IMUL eax, ebx ; multiplicando dois inteiros
	MOV [fatorialx], eax
	MOV eax, 1
	MOV ebx, [aux]
	SUB eax, ebx ; subtraindo dois inteiros
	MOV [aux], eax

	MOV ebx, [aux] ; inicia uma comparacao
	MOV ecx, 0
	CMP ebx, ecx
	JL label_9
	JMP label_12
	MOV eax, [fatorialx]
	MOV ebx, [fatorialp]
	IMUL eax, ebx ; multiplicando dois inteiros
	MOV [denominador], eax
	MOV eax, [denominador]
	MOV ebx, [fatorialn]
	DIV eax ; dividindo dois inteiros
	MOV [resultado], eax

	MOV eax, [resultado]
	PUSH eax 
	PUSH in_out; escrevendo string em tela
	CALL printf
	MOV eax, 1
	MOV ebx, [colunaatual]
	ADD eax, ebx ; somando dois inteiros
	MOV [colunaatual], eax

	MOV eax, [n]
	PUSH eax 
	PUSH in_out; escrevendo string em tela
	CALL printf
	MOV eax, 1
	MOV ebx, [linhaatual]
	ADD eax, ebx ; somando dois inteiros
	MOV [linhaatual], eax
	MOV eax, 1
	MOV ebx, [linhaatual]
	ADD eax, ebx ; somando dois inteiros
	MOV [x], eax

	MOV ebx, [colunaatual] ; inicia uma comparacao
	MOV ecx, [x]
	CMP ebx, ecx
	JG label_3
	JMP label_12

	MOV ebx, [linhaatual] ; inicia uma comparacao
	MOV ecx, [linhastotal]
	CMP ebx, ecx
	JG label_1
	JMP label_12

label_12:

label_11:

	PUSH string0; escrevendo string em tela
	CALL printf
	JMP label_0

label_13:
	RET