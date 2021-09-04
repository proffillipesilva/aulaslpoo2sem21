def fatorial(n):
  produto = 1
  for i in range(1,n+1):
    produto *= i
    return produto

    def main():
      for i in range(20):
        print( fatorial(i))

      main()
