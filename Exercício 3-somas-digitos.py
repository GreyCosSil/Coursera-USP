numero = int(input("Digite um número inteiro: "))

milhao1 = numero//100000000
milhao2 = (numero%100000000)//10000000
milhao3 = ((numero%100000000)%10000000)//1000000
milhar1 = (((numero%100000000)%10000000)%1000000)//100000
milhar2 = ((((numero%100000000)%10000000)%1000000)%100000)//10000
milhar3 = (((((numero%100000000)%10000000)%1000000)%100000)%10000)//1000
centena = ((((((numero%100000000)%10000000)%1000000)%100000)%10000)%1000)//100
dezena = (((((((numero%100000000)%10000000)%1000000)%100000)%10000)%1000)%100)//10
unidade = (((((((numero%100000000)%10000000)%1000000)%100000)%10000)%1000)%100)%10

soma = milhao1+milhao2+milhao3+milhar1+milhar2+milhar3+centena+dezena+unidade
print(soma)
		
				
	


