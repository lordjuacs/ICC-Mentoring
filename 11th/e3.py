from random import *

lista = [randint(1, 100) for i in range(10)]
cuadrados = [x ** 2 for x in lista]
otros = sorted(lista + cuadrados)[4:]
cont = 0
print(otros)
print(lista)
print(cuadrados)
matriz = [[otros[i * 4 + j] for j in range(4)] for i in range(4)]
print(matriz)
