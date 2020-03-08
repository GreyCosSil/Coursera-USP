import math

x1 = float(input('Digite o primeiro ponto x: '))
y1 = float(input('Digite o primeiro ponto y: '))
x2 = float(input('Digite o segundo ponto x: '))
y2 = float(input('Digite o segundo ponto y: '))

if((math.sqrt((x1-x2)**2+(y1-y2)**2)) >= 10):
	print('longe')
else:	
	print('perto')

