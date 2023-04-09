from datetime import datetime

objetivo = int(input('Escoge un número => '))
tiempo_inicial = datetime.now()
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0
iteraciones = 1

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    iteraciones += iteraciones
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raiz cuadrada {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

tiempo_final = datetime.now()
print(f'Duración: {tiempo_final - tiempo_inicial}')