import math
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = ((b**2)-(4*a*c))

if delta >= 0 : 
	
	raiz1 = ((-b+math.sqrt(delta))/(2*a))	
	raiz2 = ((-b-math.sqrt(delta))/(2*a))
	
	if delta == 0:
		print("a raiz desta equação é "+str(raiz1))
	else:
		
	
		if(raiz2 > raiz1):
			print("as raízes da equação são "+str(raiz1)+" e "+str(raiz2))
		else:
			print("as raízes da equação são "+str(raiz2)+" e "+str(raiz1))

else:
	print("esta equação não possui raízes reais")
