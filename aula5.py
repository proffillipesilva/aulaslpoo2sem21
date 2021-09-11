def media(valor):
	soma = 0
	media = 0
	lista = valor.split("\n")
	for numero in lista:
		soma += int(numero)
	media = soma/len(lista)
	return media
valor = """1111111111111
21094755
221
31451
446662
14141
1992"""
print(media(valor))
