C:
cd "C:\Users\muca_\AppData\Local\bin\NASM"
nasm -f elf "D:\Programação\compiladores\assembly\saida_assembly.asm"
gcc -m32 -o -target "D:\Programação\compiladores\assembly\saida_assembly.o"
-target.exe
pause