def maior_elemento(lista):
    i = 0
    maior = lista[0]
    while i < len(lista):
        if lista[i] > maior:
            maior = lista[i]
        i += 1
    return maior
    
