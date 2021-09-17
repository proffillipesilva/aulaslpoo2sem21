
def impares(num):
    if num % 2 != 0:
        return True
    else:
        return False

def filtro(lista, condicao):
    filtrados = []
    for elemento in lista:
        if condicao(elemento):
            filtrados.append(elemento)
    return filtrados

def eleva_ao_quadrado(num):
    return num*num

def mapear(lista, transformacao):
    mapeados = []
    for elemento in lista:
        transformado = transformacao(elemento)
        mapeados.append(transformado)
    return mapeados


if __name__ == '__main__':
    lista = [8,0,1,2,4,9,6,8,11,14,18,24,29]
    resultado = mapear(lista, eleva_ao_quadrado)
    print(lista)
    print(resultado)

