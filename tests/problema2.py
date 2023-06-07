linhas_total = int(input("Quantas linhas: "))

linha_atual = 0
coluna_atual = 0
fatorial_n = 1
fatorial_p = 1
fatorial_x = 1

if linhas_total >= 1:
    while (linha_atual < linhas_total):
        coluna_atual = 0     
        fatorial_n = 1
        fatorial_p = 1
        fatorial_x = 1
        while (coluna_atual < linha_atual + 1):
            fatorial_n = 1
            fatorial_p = 1
            fatorial_x = 1
            # n!
            n = linha_atual
            while (n > 0):
                fatorial_n = fatorial_n * n
                n = n - 1
            
            # p!
            p = coluna_atual
            while (p > 0):
                fatorial_p = fatorial_p * p
                p = p - 1
            
            # (n - p)!
            aux = linha_atual - coluna_atual
            while (aux > 0):
                fatorial_x = fatorial_x * aux
                aux = aux - 1

            denominador =  fatorial_p * fatorial_x
            resultado = fatorial_n / denominador
            print(int(resultado), end="")
            print(" ", end="")
            coluna_atual = coluna_atual + 1
            
        print("")
        linha_atual = linha_atual + 1
