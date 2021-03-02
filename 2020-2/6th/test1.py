import math
"""matriz = [[1, 2, 5], [3, 4, 7]]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()

a = int(input("Ingrese total de alumnos: "))
n = int(input("Ingrese total de notas: "))
matrix = []
for i in range(a):
    notas = []
    for j in range(n):
        f = int(input("Persona " + str(i+1) + " nota " + str(j+1) + ":"))
        notas.append(f)
    matrix.append(notas)
promedio = []
for lista in matrix:
    promedio.append(sum(lista)/len(lista))
for p in promedio:
    print(p, end=" ")
"""
def multiplicar(n, veces):
    if veces == 1:
        return n
    return n + multiplicar(n, veces - 1)
def sumados(a, b):
    return a + b
def factorial(n):
    if n < 0:
        print("No tiene")
    if n == 0 or n == 1:
        return n
    return n * factorial(n - 1)

title = "2017 2018"
print(title.rjust(22, ' '))












