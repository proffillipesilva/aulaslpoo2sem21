if __name__ == '__main__':


	print('Olá Fiec!')

	"""
	Você recebe duas notas (nota1 e nota2).
	Se a média for no mínimo 6 imprima "passou"
	Caso contrário, imprima Errou
	"""

	# O \r\n faz com que se pule uma linha (CRLF)
	nota1 = float(input("insira nota1: \r\n"))
	nota2 = float(input("insira nota2: \r\n"))
	media = (nota1+nota2)/2

	if media >= 6:
		print("Passou")
	else:
		print("Errou")
