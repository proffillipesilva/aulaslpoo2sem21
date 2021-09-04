def fatorial(n):
	produto = n
	for i in range (1, n):
		produto = produto * (n-1)
	return produto 

def main():
	for i in range (10):
		print (fatorial(i))
main()
