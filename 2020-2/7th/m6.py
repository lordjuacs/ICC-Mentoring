def generar_matriz(filas ,columnas, elemento = 'U'):
    matriz = []
    for i in range(filas):
        lista = []
        for j in range(columnas):
            lista.append(elemento)
        matriz.append(lista)
    return matriz

matriz = generar_matriz(7, 1)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end= " ")
    print()