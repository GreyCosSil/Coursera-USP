
import math

def é_hipotenusa(x,y):
    
    global matriz
    global somasHip
    global result
    global result1
    global entrou
    
    if x % 1 == 0 and x <= y:
        for x in matriz:
            result = 1
            result1 = 0
        entrou = 1
    return result
    return result1

def soma_hipotenusas(n):
    
    global matriz
    global somasHip
    global result
    global result1
    global entrou

    result = 0
    result1 = 1
    entrou = 0    
    matriz = []
    
    i = 1
    somasHip = 0
    
    while i <= n:
        j = 1
        while j <= n:
            raiz = math.sqrt(i**2 + j**2)
            é_hipotenusa(raiz, n)
            if entrou == 1:
                if result == 1 and result1 == 0:
                    result = 0
                    result1 = 1
                else:
                    somasHip = somasHip + raiz
                    result = 0
                    result1 = 1
                entrou = 0
            j += 1
            continue
        i = i+1
        continue

    print(somasHip)

soma_hipotenusas(25)
