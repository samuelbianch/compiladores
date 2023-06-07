section .data ; declara constantes
	in_out DB "%d", 0x0
	string0: DB 'LOOP', 10, 0
	string1: DB 'EntreiNoOutroEnquanto', 10, 0


section .bss ; declara as variaveis
   a: RESD 1
   i: RESD 1


section .text ; importa scanf e printf do gcc compiler
	global main
	extern printf
	extern scanf

main:

	MOV eax, 4; recebendo um numero inteiro
	MOV [a], eax
	MOV eax, 0; recebendo um numero inteiro
	MOV [i], eax

label_0:

label_1:
	MOV ebx, [i] ; inicia uma comparacao 
	MOV ecx, [a] 
	CMP ebx, ecx 
	JG label_2

	PUSH string0; escrevendo string em tela
	CALL printf
	MOV ebx, [i] ; inicia uma comparacao 
	MOV ecx, 2 
	CMP ebx, ecx 
	JG label_2

	PUSH string1; escrevendo string em tela
	CALL printf
	MOV eax, 1
	MOV ebx, [i]
	ADD eax, ebx ; somando dois inteiros
	MOV [i], eax
	JMP label_0
	MOV eax, 1
	MOV ebx, [i]
	ADD eax, ebx ; somando dois inteiros
	MOV [i], eax

label_2:
	RET