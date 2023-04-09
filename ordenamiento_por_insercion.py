import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice
        print(posicion_actual, valor_actual)

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista


if __name__ == '__main__':
    list_size = int(input('De que tamaño será la lista? '))

    list = [random.randint(0, 100) for i in range(list_size)]
    print(list)

    list_ordered = ordenamiento_por_insercion(list)
    print(list_ordered)