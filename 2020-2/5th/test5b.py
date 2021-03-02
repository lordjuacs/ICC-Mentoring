"""Diseñar una función recursiva para hallar el número máximo de una lista o un array.

Input Format

Lista de elementos. Se detiene cuando se ingresa el 0"""


def max_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    return max(max_lista_rec(lista[1:]), lista[0])


lista = []
while True:
    n = int(input())
    if n == 0:
        break
    lista.append(n)
print(max_lista_rec(lista))
