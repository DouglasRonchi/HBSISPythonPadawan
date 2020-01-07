def find_short(frase):
	menor = 99
	for palavra in frase.split():
		if len(palavra) < menor:
			menor = len(palavra)
	return menor
