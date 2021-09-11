def cauculo_media(texto):
	soma = 0
	media = 0
	lista = texto.split("\n")
	for numero in lista:
		soma += int(numero)
	media = soma/len(lista)
	return media
texto = """4
2
5
2
3
4
6
8"""
print(cauculo_media(texto))
