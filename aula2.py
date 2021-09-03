def monstro():
	nota1= int (input("valor nota 1:  "))
	nota2= int (input("valor nota 2:  "))

	Soma= nota1 + nota2

	Media= Soma / 2

	if Media >= 5:
		print ("passou")
	else:
		print ("bombou")

monstro()
