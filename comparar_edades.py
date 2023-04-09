name_first = input('Digite el nombre de la primera persona => ')
age_first = int(input(f'Digite la edad de {name_first} => '))
name_second = input('Digite el nombre de la segunda persona => ')
age_second = int(input(f'Digite la edad de {name_second} => '))

if age_first > age_second:
    print(f'{name_first} tiene más edad que {name_second}')
elif age_first < age_second:
    print(f'{name_second} tiene más edad que {name_first}')
else:
    print(f'{name_first} y {name_second} tienen la misma edad')
