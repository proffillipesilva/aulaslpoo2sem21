def fatorial(n):
	num = 1
	for i in range(1,n+1):
		num *= i
	return num 

def main():
	print(fatorial(4))

main()
