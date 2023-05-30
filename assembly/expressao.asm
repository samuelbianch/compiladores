section .data
    hello: db "Hello World", 10, 0
    
section .bss

section .text
    global _main
    extern _printf

_main:
    CONST equ (5*4-(8/4)) / 3
    MOV eax, CONST
    PUSH eax
    CALL _printf
    RET