def fatorial(n):
	resultado = n
	for i in range(1, n):
		resultado = resultado * (n-i)
	return resultado
def main():
	for i in range(10):
		print(fatorial(i))
main()
