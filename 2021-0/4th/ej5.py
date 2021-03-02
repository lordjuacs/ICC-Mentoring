from random import *

lista = [randint(1, 100) for i in range(100)]

visitados = []
ocurrencias = []
for i in lista:
    if i not in visitados:
        ocurrencias.append(lista.count(i))
        visitados.append(i)

final = []
valor = max(ocurrencias)
count = 0
while count < 3:
    for i in range(len(visitados)):
        if ocurrencias[i] == valor and count < 3:
            final.append(visitados[i])
            count += 1
            if count == 3:
                break
    valor -= 1
print("Suma de tres mas repetidos:", sum(final))