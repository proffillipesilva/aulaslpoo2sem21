def fatorial (n) :
	produto = 1
	for i in range(1, n):
			produto *= i
	return produto

def main ():
	for i in range (10):
			print(fatorial(i))
main ()
