import random

matriz = []
n = 100
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(random.randint(1, 5))
    matriz.append(fila)
for i in range(n):
    for j in range(n):
        print(matriz[i][j], end=" ")
    print()
suma_fil = 0
filas = []

for i in range(n):
    for j in range(n):
        suma_fil += matriz[i][j]
    filas.append(suma_fil)
    suma_fil = 0
for i in range(n):
    print("Suma fila " + str(i + 1) + ":", filas[i])
suma_col = 0
cols = []
print()
for i in range(n):
    for j in range(n):
        suma_col += matriz[j][i]
    cols.append(suma_col)
    suma_col = 0
for i in range(n):
    print("Suma col " + str(i + 1) + ":", cols[i])
