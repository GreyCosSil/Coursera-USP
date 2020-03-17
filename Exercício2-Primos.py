def maior_primo(x):
	while x >= 2:
		if x == 2:
			return x
			break
		else:
			if x != 3 and x != 5 and x != 7:
				if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 and x%31!=0:
					return x
					break				
				else:	
					x -= 1
					continue
			else:
				return x
				break

	
print(maior_primo(961))
