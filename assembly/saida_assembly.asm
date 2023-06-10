section .data ; declara constantes
	in_out DB "%d", 0x0
	string0: DB 'NaoEhTriangulo', 10, 0
	string1: DB 'Equilatero', 10, 0
	string2: DB 'Isoceles', 10, 0
	string3: DB 'Isoceles', 10, 0
	string4: DB 'Isoceles', 10, 0
	string5: DB 'Escaleno', 10, 0


section .bss ; declara as variaveis
   a: RESD 1
   aux1: RESD 1
   aux2: RESD 1
   aux3: RESD 1
   b: RESD 1
   c: RESD 1
   resposta: RESD 1


section .text ; importa scanf e printf do gcc compiler
	global main
	extern printf
	extern scanf

main:


	PUSH a; lendo uma entrada
	PUSH in_out
	CALL scanf

	PUSH b; lendo uma entrada
	PUSH in_out
	CALL scanf

	PUSH c; lendo uma entrada
	PUSH in_out
	CALL scanf
	MOV eax, [b]
	MOV ebx, [a]
	ADD eax, ebx ; somando dois inteiros
	MOV [aux1], eax
	MOV eax, [c]
	MOV ebx, [a]
	ADD eax, ebx ; somando dois inteiros
	MOV [aux2], eax
	MOV eax, [c]
	MOV ebx, [b]
	ADD eax, ebx ; somando dois inteiros
	MOV [aux3], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [resposta], eax

label_0:
	MOV ebx, [aux1] ; inicia uma comparacao 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JG label_1
	MOV eax, 0; recebendo um numero inteiro
	MOV [resposta], eax

label_1:
	MOV ebx, [aux2] ; inicia uma comparacao 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JG label_2
	MOV eax, 0; recebendo um numero inteiro
	MOV [resposta], eax

label_2:
	MOV ebx, [aux3] ; inicia uma comparacao 
	MOV ecx, [a] 
	CMP ebx, ecx 
	JG label_3
	MOV eax, 0; recebendo um numero inteiro
	MOV [resposta], eax

label_3:
	MOV ebx, [resposta] ; inicia uma comparacao 
	MOV ecx, 0 
	CMP ebx, ecx 
	JNE label_4

	PUSH string0; escrevendo string em tela
	CALL printf
	RET

label_5:

label_6:

label_7:

label_4:
	MOV ebx, [a] ; inicia uma comparacao 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JNE label_8
	MOV ebx, [b] ; inicia uma comparacao 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JNE label_8

	PUSH string1; escrevendo string em tela
	CALL printf
	RET

label_8:

label_9:
	MOV ebx, [a] ; inicia uma comparacao 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JNE label_10
	MOV ebx, [b] ; inicia uma comparacao 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JE label_10

	PUSH string2; escrevendo string em tela
	CALL printf
	RET

label_10:

label_11:
	MOV ebx, [b] ; inicia uma comparacao 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JNE label_12
	MOV ebx, [b] ; inicia uma comparacao 
	MOV ecx, [a] 
	CMP ebx, ecx 
	JE label_12

	PUSH string3; escrevendo string em tela
	CALL printf
	RET

label_12:

label_13:
	MOV ebx, [a] ; inicia uma comparacao 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JNE label_14
	MOV ebx, [c] ; inicia uma comparacao 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JE label_14

	PUSH string4; escrevendo string em tela
	CALL printf
	RET

label_14:

label_15:
	MOV ebx, [a] ; inicia uma comparacao 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JE label_16
	MOV ebx, [a] ; inicia uma comparacao 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JE label_16

	PUSH string5; escrevendo string em tela
	CALL printf
	RET

label_16:
	RET