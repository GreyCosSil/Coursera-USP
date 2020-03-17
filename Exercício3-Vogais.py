def vogal(x):
	
	if (type (x)) == str:
		if x.casefold() != "a" and x.casefold() != "e" and x.casefold() != "i" and x.casefold() != "o" and x.casefold() != "u":
			return(bool(0))
		else: 
			return(bool(1))
	else:
		return("Invalido")


