C:
cd "C:\Users\muca_\AppData\Local\bin\NASM"
nasm -fwin32 "D:\Programação\compiladores\assembly\saida_assembly.asm"
gcc -m32 "D:\Programação\compiladores\assembly\saida_assembly.obj" -o "D:\Programação\compiladores\assembly\saida_assembly.exe"
"D:\Programação\compiladores\assembly\saida_assembly.exe"
pause