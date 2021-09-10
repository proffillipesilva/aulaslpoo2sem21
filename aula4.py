def soma(lista):
    soma = 0
    for valor in lista:
        soma += valor
    return soma

listaSoma = [1, 3, 3, 6, 5, 6, 7]

print(soma(listaSoma))
