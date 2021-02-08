from random import *


def generarmatriz(n, m):
    matriz = []
    for i in range(n):
        lista = []
        for j in range(m):
            lista.append(randint(0, 10))
        matriz.append(lista)
    return matriz


def imprimirmatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()


def transformarmatriz(matriz):
    if len(matriz) == len(matriz[0]):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if i % 2 == 0:
                    matriz[i][j] += 1
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if i % 2 != 0:
                    matriz[i][j] *= 2
    return matriz


def sumacolumnas(matriz):
    suma = []
    for j in range(len(matriz[0])):
        acumulado = 0
        for i in range(len(matriz)):
            acumulado += matriz[i][j]
        suma.append(acumulado)
    return suma


while True:
    n = int(input("Ingrese numero de filas: "))
    if n > 1:
        break
while True:
    m = int(input("Ingrese numero de columnas: "))
    if m > 1:
        break

matriz = generarmatriz(n, m)
print("Matriz original")
imprimirmatriz(matriz)
matrizfinal = transformarmatriz(matriz)
print("Matriz final")
imprimirmatriz(matrizfinal)
print("Suma columnas:", sumacolumnas(matrizfinal))
