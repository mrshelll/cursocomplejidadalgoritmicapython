import random

def busqueda_binaria(list, start, end, index):
    if start > end:
        return False
    
    middle = (start + end) // 2

    if list[middle] == index:
        return True
    elif list[middle] < index:
        return busqueda_binaria(list, middle + 1, end, index)
    else:
        return busqueda_binaria(list, start, middle - 1, index)

if __name__ == '__main__':
    list_size = int(input('De que tamaño será la lista? '))
    index = int(input('Qué número quieres encontrar? '))

    list = sorted([random.randint(0, 100) for i in range(list_size)])

    found = busqueda_binaria(list, 0, len(list), index)
    print(list)
    print(f'El elemento {index} {"está" if found else "no está"} en la lista' )