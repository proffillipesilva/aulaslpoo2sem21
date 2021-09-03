def main():
    nota1 = int (input("insira nota1:   "))
    nota2 = int (input("insira nota2:   "))

    soma = nota1 + nota2

    media = soma / 2

    if media >= 5 :
    	print ("Passou")
    else:
    	print ("Bombou")

main()
