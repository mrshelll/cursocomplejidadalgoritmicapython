import random

def busqueda_lineal(list, objetivo):
    match = False

    for element in list: # O(n)
        if element == objetivo:
            match = True
            break

    return match

if __name__ == '__main__':
    list_size = int(input('De que tamaño será la lista? '))
    index = int(input('Qué número quieres encontrar? '))

    list = [random.randint(0, 100) for i in range(list_size)]

    found = busqueda_lineal(list, index)
    print(list)
    print(f'El elemento {index} {"está" if found else "no está"} en la lista' )