section .data
    hello: db "Hello World", 10, 0
    
section .bss

section .text
    global main
    extern printf

main:
    mov ebp, esp; for correct debugging
    CONST equ (5*4-(8/4)) / 3
    MOV eax, CONST
    PUSH eax
    CALL printf
    RET