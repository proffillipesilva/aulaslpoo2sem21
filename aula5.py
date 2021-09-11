def media(frase):
	soma = 0 
	media = 0
	lista = frase.split("\n")
	for numero in lista:
		soma += int(numero)
	media = soma/len(lista)
	return media
frase = """9
5
5
2
1
4"""
print(media(frase))
