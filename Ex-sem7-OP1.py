
def n_primos(n):
    valor = 2
    result = 0
    primo = 0

    while n >= 2:
        if n == 2:
            result = 1

        while n > valor:
            if valor == 2:
                result = 1
                valor += 1
            while valor > 2 and valor <= n:
                primo = 2

                while primo < valor and primo > 1:
	                if valor % primo == 0:
                        primo += 1
			        else:
				        result = result + 1
			            primo += 1

            valor += 1
        print(result)

n_primos(4)
