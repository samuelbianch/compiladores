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
	MOV ebx, [linhastotal] ; inicia uma comparacao 
	MOV ecx, 1 
	CMP ebx, ecx 
	JL label_3
	MOV eax, 0; recebendo um numero inteiro
	MOV [colunaatual], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialn], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialp], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialx], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialn], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialp], eax
	MOV eax, 1; recebendo um numero inteiro
	MOV [fatorialx], eax
	MOV ebx, [linhaatual]
	MOV [n], ebx ; recebe um valor apos a operacao

	MOV ebx, [f] ; iniciando uma operacao aritmetica
	MOV ecx, [a]

	MOV ebx, [o] ; iniciando uma operacao aritmetica
	MOV ecx, [r]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [l]

	MOV ebx, [ ] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]
	MUL ebx, ecx
	MOV ebx, [fatorialn  n*]
	MOV [fatorialn], ebx ; recebe um valor apos a operacao

	MOV ebx, [n] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]

	MOV ebx, [1] ; iniciando uma operacao aritmetica
	SUB ebx, ecx
	MOV ebx, [n  1-]
	MOV [n], ebx ; recebe um valor apos a operacao

label_3:
	MOV ebx, [colunaatual]
	MOV [p], ebx ; recebe um valor apos a operacao

label_2:

	MOV ebx, [f] ; iniciando uma operacao aritmetica
	MOV ecx, [a]

	MOV ebx, [o] ; iniciando uma operacao aritmetica
	MOV ecx, [r]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [l]

	MOV ebx, [ ] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]
	MUL ebx, ecx
	MOV ebx, [fatorialp  p*]
	MOV [fatorialp], ebx ; recebe um valor apos a operacao

	MOV ebx, [p] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]

	MOV ebx, [1] ; iniciando uma operacao aritmetica
	SUB ebx, ecx
	MOV ebx, [p  1-]
	MOV [p], ebx ; recebe um valor apos a operacao

	MOV ebx, [l] ; iniciando uma operacao aritmetica
	MOV ecx, [i]

	MOV ebx, [h] ; iniciando uma operacao aritmetica
	MOV ecx, [a]

	MOV ebx, [t] ; iniciando uma operacao aritmetica
	MOV ecx, [u]

	MOV ebx, [l] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]

	MOV ebx, [c] ; iniciando uma operacao aritmetica
	MOV ecx, [o]

	MOV ebx, [u] ; iniciando uma operacao aritmetica
	MOV ecx, [n]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [t]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [l]
	SUB ebx, ecx
	MOV ebx, [linhaatual  colunaatual-]
	MOV [aux], ebx ; recebe um valor apos a operacao

label_14:

	MOV ebx, [f] ; iniciando uma operacao aritmetica
	MOV ecx, [a]

	MOV ebx, [o] ; iniciando uma operacao aritmetica
	MOV ecx, [r]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [l]

	MOV ebx, [ ] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]

	MOV ebx, [u] ; iniciando uma operacao aritmetica
	MOV ecx, [x]
	MUL ebx, ecx
	MOV ebx, [fatorialx  aux*]
	MOV [fatorialx], ebx ; recebe um valor apos a operacao

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [u]

	MOV ebx, [ ] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]
	SUB ebx, ecx
	MOV ebx, [aux  1-]
	MOV [aux], ebx ; recebe um valor apos a operacao

	MOV ebx, [f] ; iniciando uma operacao aritmetica
	MOV ecx, [a]

	MOV ebx, [o] ; iniciando uma operacao aritmetica
	MOV ecx, [r]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [l]

	MOV ebx, [ ] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [t]

	MOV ebx, [r] ; iniciando uma operacao aritmetica
	MOV ecx, [i]

	MOV ebx, [l] ; iniciando uma operacao aritmetica
	MOV ecx, [x]
	MUL ebx, ecx
	MOV ebx, [fatorialp  fatorialx*]
	MOV [denominador], ebx ; recebe um valor apos a operacao

	MOV ebx, [f] ; iniciando uma operacao aritmetica
	MOV ecx, [a]

	MOV ebx, [o] ; iniciando uma operacao aritmetica
	MOV ecx, [r]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [l]

	MOV ebx, [ ] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]

	MOV ebx, [e] ; iniciando uma operacao aritmetica
	MOV ecx, [n]

	MOV ebx, [m] ; iniciando uma operacao aritmetica
	MOV ecx, [i]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [d]

	MOV ebx, [r] ; iniciando uma operacao aritmetica
	DIV ebx, ecx
	MOV ebx, [fatorialn  denominador/]
	MOV [resultado], ebx ; recebe um valor apos a operacao

	PUSH string0; escrevendo string em tela
	CALL printf

	MOV ebx, [c] ; iniciando uma operacao aritmetica
	MOV ecx, [o]

	MOV ebx, [u] ; iniciando uma operacao aritmetica
	MOV ecx, [n]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [t]

	MOV ebx, [a] ; iniciando uma operacao aritmetica
	MOV ecx, [l]

	MOV ebx, [ ] ; iniciando uma operacao aritmetica
	MOV ecx, [1]
	ADD ebx, ecx
	MOV ebx, [colunaatual  1+]
	MOV [colunaatual], ebx ; recebe um valor apos a operacao

	PUSH string1; escrevendo string em tela
	CALL printf

	MOV ebx, [l] ; iniciando uma operacao aritmetica
	MOV ecx, [i]

	MOV ebx, [h] ; iniciando uma operacao aritmetica
	MOV ecx, [a]

	MOV ebx, [t] ; iniciando uma operacao aritmetica
	MOV ecx, [u]

	MOV ebx, [l] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]

	MOV ebx, [1] ; iniciando uma operacao aritmetica
	ADD ebx, ecx
	MOV ebx, [linhaatual  1+]
	MOV [linhaatual], ebx ; recebe um valor apos a operacao

	MOV ebx, [l] ; iniciando uma operacao aritmetica
	MOV ecx, [i]

	MOV ebx, [h] ; iniciando uma operacao aritmetica
	MOV ecx, [a]

	MOV ebx, [t] ; iniciando uma operacao aritmetica
	MOV ecx, [u]

	MOV ebx, [l] ; iniciando uma operacao aritmetica
	MOV ecx, [ ]

	MOV ebx, [1] ; iniciando uma operacao aritmetica
	ADD ebx, ecx
	MOV ebx, [linhaatual  1+]
	MOV [x], ebx ; recebe um valor apos a operacao

label_15:

	PUSH string2; escrevendo string em tela
	CALL printf
	RET

label_17: