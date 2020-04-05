import math
def soma_hipotenusas(n):
    global matriz
    matriz = []
    while n >= 1 and n % 1 == 0:
        é_hipotenusa(n)
        for x in matriz:
            
        print (matriz)
        break
    return result
    

    
def é_hipotenusa(x):
    global raiz
    i = 0
    while i < x:
        i += 1
        j = 0
        while j < x:
            j += 1
            raiz = math.sqrt(i**2 + j**2)
            if raiz % 1 == 0:
                return raiz
                    
    
