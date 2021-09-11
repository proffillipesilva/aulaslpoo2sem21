def fatorial(n):
	total = n
	for i in range(1, n):
		total = total * (n-i)
	return total
def main():
	for i in range(15):
		print(fatorial(i))
main()
