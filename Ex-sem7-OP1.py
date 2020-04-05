def n_primos(n):
    global primos
    primos = 0
    while n >= 2:
        if n == 2:
            primos = 1
            break
        else:
            ePrimo(n)
            primos = primo
            break
    print(primos)
            
def ePrimo(x):
    global primo
    primo = 1
    InesimoN = 3
    i = 2
    status = "indefinido"
    while InesimoN  <= x:
        while i < InesimoN:
            if InesimoN % i != 0 and InesimoN > i:
                i += 1
                status = "sim"
            else:
                status = "nao"
                break

        if status == "sim":
            primo += 1
                
        InesimoN += 1
        i = 2

    return primo    

n_primos(121)
