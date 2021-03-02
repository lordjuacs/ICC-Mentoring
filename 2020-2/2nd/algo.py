#ej 1
"""n = int(input())

for i in range(0, n +1, 2):
    print(i)

#ej 2
print("Hallar el promedio")
a = 0
b = 0
print("para terminar, ingrese 0")
x = float(input("Ingresa los números: "))
while x != 0:
    a += x
    b += 1
    x = float(input("Ingresa los números: "))
    if x == 0:
        promedio = a / b
        print("El promedio es: ", promedio)

a = 0
b = 0
while True:
    x = float(input("Ingresa los numeros: "))
    if x == 0:
        break
    a += x
    b += 1
if x != 0:
    promedio = a / b
    print("El promedio es: ", promedio)

#ej 3
cant = int(input("Ingrese cantidad: "))

for i in range(1, cant + 1):
    print(i**2)

y=int(input("numero:"))
n=0
while n < y:
    print((n+1)**2)
    n=n+1
"""
#ej 4
numero = int(input("Ingrese un numero: "))
for i in range(1, 10):
    print(str(numero) + "x" + str(i) + " = " + str(i*numero))