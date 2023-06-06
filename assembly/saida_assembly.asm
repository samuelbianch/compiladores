section .data ; declara constantes
	in_out DB "%d", 0x0
	string0: DB 'EhTriangulo', 10, 0
	string1: DB 'Equilatero', 10, 0
	string2: DB 'Isoceles', 10, 0
	string3: DB 'Isoceles', 10, 0
	string4: DB 'Escaleno', 10, 0
	string5: DB 'ERRO', 10, 0
	string6: DB 'NaoEhTriangulo', 10, 0


section .bss ; declara as variaveis
   a: RESD 1
   aux1: RESD 1
   aux2: RESD 1
   aux3: RESD 1
   b: RESD 1
   c: RESD 1


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

	MOV ebx, a
	MOV ecx, b
	ADD ebx, ecx
	MOV [aux1], ebx

	MOV ebx, a
	MOV ecx, c
	ADD ebx, ecx
	MOV [aux2], ebx

	MOV ebx, b
	MOV ecx, c
	ADD ebx, ecx
	MOV [aux3], ebx
	MOV ebx, [aux1] 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JL label_5
	MOV ebx, [aux2] 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JL label_5
	MOV ebx, [aux3] 
	MOV ecx, [a] 
	CMP ebx, ecx 
	JL label_5

	PUSH string0; escrevendo string em tela
	CALL printf
	MOV ebx, [a] 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JNE label_5
	MOV ebx, [b] 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JNE label_5

	PUSH string1; escrevendo string em tela
	CALL printf
	RET

label_5:
	MOV ebx, [a] 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JNE label_15
	MOV ebx, [b] 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JE label_15

	PUSH string2; escrevendo string em tela
	CALL printf
	RET

label_15:
	MOV ebx, [b] 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JNE label_21
	MOV ebx, [b] 
	MOV ecx, [a] 
	CMP ebx, ecx 
	JE label_21

	PUSH string3; escrevendo string em tela
	CALL printf
	RET

label_21:
	MOV ebx, [a] 
	MOV ecx, [b] 
	CMP ebx, ecx 
	JE label_27
	MOV ebx, [a] 
	MOV ecx, [c] 
	CMP ebx, ecx 
	JE label_27

	PUSH string4; escrevendo string em tela
	CALL printf
	RET

label_27:

label_30:

	PUSH string5; escrevendo string em tela
	CALL printf
	RET

label_32:

label_34:

	PUSH string6; escrevendo string em tela
	CALL printf
	RET

label_36: