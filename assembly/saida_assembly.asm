section .data ; declara constantes
	in_out DB "%d", 0x0
	string0: DB 'Equilatero', 10, 0
	string1: DB 'Isoceles', 10, 0
	string2: DB 'Isoceles', 10, 0
	string3: DB 'Escaleno', 10, 0
	string4: DB 'ERRO', 10, 0
	string5: DB 'NaoEhTriangulo', 10, 0


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

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [b]
	ADD ebx, ecx
	MOV [aux1], ebx ; recebe um valor apos a operacao

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [c]
	ADD ebx, ecx
	MOV [aux2], ebx ; recebe um valor apos a operacao

	MOV ebx, [b] ; iniciando uma operacao aritmetica
	MOV ecx, [c]
	ADD ebx, ecx
	MOV [aux3], ebx ; recebe um valor apos a operacao
	MOV eax, 1; recebendo um numero inteiro
	MOV [resposta], eax
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
	JG label_4
	MOV eax, 0; recebendo um numero inteiro
	MOV [resposta], eax

label_4:
	MOV ebx, [aux3] ; inicia uma comparacao 
	MOV ecx, [a] 
	CMP ebx, ecx 
	JG label_7
	MOV eax, 0; recebendo um numero inteiro
	MOV [resposta], eax

label_7:
	MOV ebx, [resposta] ; inicia uma comparacao 
	MOV ecx, 1 
	CMP ebx, ecx 
	JNE label_12
	MOV ebx, [a] ; inicia uma comparacao 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JNE label_12
	MOV ebx, [b] ; inicia uma comparacao 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JNE label_12

	PUSH string0; escrevendo string em tela
	CALL printf
	RET

label_12:
	MOV ebx, [a] ; inicia uma comparacao 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JNE label_18
	MOV ebx, [b] ; inicia uma comparacao 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JE label_18

	PUSH string1; escrevendo string em tela
	CALL printf
	RET

label_18:
	MOV ebx, [b] ; inicia uma comparacao 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JNE label_23
	MOV ebx, [b] ; inicia uma comparacao 
	MOV ecx, [a] 
	CMP ebx, ecx 
	JE label_23

	PUSH string2; escrevendo string em tela
	CALL printf
	RET

label_23:
	MOV ebx, [a] ; inicia uma comparacao 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JE label_28
	MOV ebx, [a] ; inicia uma comparacao 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JE label_28

	PUSH string3; escrevendo string em tela
	CALL printf
	RET

label_28:

label_30:

	PUSH string4; escrevendo string em tela
	CALL printf
	RET

label_32:

label_33:

	PUSH string5; escrevendo string em tela
	CALL printf
	RET

label_35: