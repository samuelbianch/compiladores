section .data
    hello: db "Hello World", 10, 0

section .bss

section .text
    global _main
    extern _printf

_main:
    push hello
    call _printf