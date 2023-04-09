def enumeracion_exhaustiva(objetivo: int):
    respuesta = 0
    mensaje_error = ''

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 != objetivo:
        mensaje_error = f'{objetivo} no tiene una raiz cuadrada exacta'

    return mensaje_error, respuesta

def aproximacion(objetivo: int):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    iteraciones = 1
    mensaje_error = ''

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        iteraciones += iteraciones
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        mensaje_error = f'No se encontró la raiz cuadrada {objetivo}'

    return mensaje_error, respuesta

def busqueda_binaria(objetivo: int):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    mensaje_error = ''

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    return mensaje_error, respuesta


def calcular_raiz_cuadrada(opcion: int, objetivo: int):
    respuesta = 0
    mensaje_error = ''

    print('--------------------------')
    if opcion == 1:
        print('Calculando por enumeración exhaustiva...')
        mensaje_error, respuesta = enumeracion_exhaustiva(objetivo)
    elif opcion == 2:
        print('Calculando por aproximación...')
        mensaje_error, respuesta = aproximacion(objetivo)
    elif opcion == 3:
        print('Calculando por búsqueda rápida...')
        mensaje_error, respuesta = busqueda_binaria(objetivo)
    else:
        mensaje_error = 'Opción no válida'
    
    return mensaje_error, respuesta


#Inicio del programa
print('Por favor digita la opción que deseas utilizar para calcular la raíz cuadrada de un número:')
print('1. Enumeración Exhaustiva')
print('2. Aproximación')
print('3. Búsqueda rápida')
print('')
opcion = int(input('Opción => '))
objetivo = int(input('Escoge un entero => '))

mensaje_error, respuesta = calcular_raiz_cuadrada(opcion, objetivo)

if len(mensaje_error) > 0:
    print(mensaje_error)
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

#Fin del programa