#1-2
for numero in range(11):
    print(numero)

numero = 0
while numero <= 10:
    print(numero)
    numero += 1

for numero in range(10, -1, -1):
    print(numero)

numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

#3-5
for i in range(1, 8):
    print('#' * i)

for fila in range(8):
    for columna in range(8):
        print('#', end=' ')
    print()  # Salto de línea después de cada fila

for numero in range(11):
    print(f"{numero} x {numero} = {numero * numero}")

#6-8
tecnologias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tecnologia in tecnologias:
    print(tecnologia)

for numero in range(0, 101):
    if numero % 2 == 0:
        print(numero)

for numero in range(0, 101):
    if numero % 2 != 0:
        print(numero)