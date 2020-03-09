numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
	if numero == 2:
		print("primo")
	else: 
		print("não primo")	
else:
	if numero == 1:
		print("não primo")
	else:
		if numero != 3 and numero != 5 and numero != 7:
			if numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
				print("primo")
			else: 
				print("não primo")
		else:
			print("primo")

