def fatorial(n):
	resultado = n
	for i in range(1,n):
		resultado = resultado * (n - 2)
	return resultado

def main():
	print( fatorial(1) )
main()
