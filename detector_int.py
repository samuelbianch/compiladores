def detector_palavra_int(palavra):
    for c in range(0, len(palavra)):
        if palavra[c] == 'i':
            if palavra[c+1] == 'n':
                if palavra[c+2] == 't':
                    return "A palavra é int"
    
    return "A palavra não contém int"
    
    
palavra_para_teste = "Esta palavra inteiro tem"
pera = 'pera'
if pera == 'pera':
    print('Olá mundo!')
print(detector_palavra_int(palavra_para_teste))