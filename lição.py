lista = [ 8,7,5,3,2,1,0,7,9,6,1,4,3,12,3,11,9,5,7,2,4,8,19]
filtro = []
for num in lista:
	if num >= 5 and num < 10:
		filtro.append(num)
print(sorted(filtro)[-3:])
