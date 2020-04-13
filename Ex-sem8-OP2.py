def reverse_a():
    global cont
    i = 0
    valores = int(input("Digite um número: "))
    matriz = []
    while valores > 0 :
        matriz.append(valores)
        valores = int(input("Digite um número: "))
        i += 1
    matriz.reverse()
    print("")
    for z in range(0, len(matriz)):        
        print(matriz[z])


reverse_a()
