def fatorial(n):
	produto = 1	
	for i in range(1, n+1):
		produto *= i
	return produto

def main():
	print(fatorial(5))

main()
