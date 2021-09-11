def media_texto(texto):
	soma = 0
	media = 0
	lista = texto.split("\n")
	for numero in lista:
		soma += int(numero)
	media = soma/len(lista)
	return media
texto = """1
8
9
0
1
4
8
2"""
print(media_texto(texto))
