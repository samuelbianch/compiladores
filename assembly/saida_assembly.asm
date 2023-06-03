section .data ; declara constantes
	in_out DB "%d", 0x0
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

	MOV ebx, [a]
	MOV ecx, [b]
	CMP ebx, ecx
	JE label_0
	JMP label_0

	PUSH string0; escrevendo string em tela
	CALL printf
	JMP label_0

	MOV ebx, [b]
	MOV ecx, [c]
	CMP ebx, ecx
	JE label_0

label_1:

	MOV ebx, [a]
	MOV ecx, [b]
	CMP ebx, ecx
	JE label_1
	JMP label_1

	PUSH string1; escrevendo string em tela
	CALL printf
	JMP label_2

	MOV ebx, [b]
	MOV ecx, [c]
	CMP ebx, ecx
	JNE label_2

label_3:

	MOV ebx, [b]
	MOV ecx, [c]
	CMP ebx, ecx
	JE label_3
	JMP label_3

	PUSH string2; escrevendo string em tela
	CALL printf
	JMP label_4

	MOV ebx, [b]
	MOV ecx, [a]
	CMP ebx, ecx
	JNE label_4

label_5:

	MOV ebx, [a]
	MOV ecx, [b]
	CMP ebx, ecx
	JNE label_5
	JMP label_5

	PUSH string3; escrevendo string em tela
	CALL printf
	JMP label_6

	MOV ebx, [a]
	MOV ecx, [c]
	CMP ebx, ecx
	JNE label_6

label_7:

	PUSH string4; escrevendo string em tela
	CALL printf