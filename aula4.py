def main(lista_random):
	soma = 0
	for valor in lista_random:
		soma += valor
	return soma

lista_random = [47, 32, 33, 16, 97, 42, 62]

print(main(lista_random))
