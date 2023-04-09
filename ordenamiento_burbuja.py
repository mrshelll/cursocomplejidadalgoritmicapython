import random

def ordenamiento_burbuja(list):
    n = len(list)

    for i in range(n): # O(n) * O(n) = O(n * n) = O(n**2)
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


if __name__ == '__main__':
    list_size = int(input('De que tamaño será la lista? '))

    list = [random.randint(0, 100) for i in range(list_size)]
    print(list)

    list_ordered = ordenamiento_burbuja(list)
    print(list_ordered)