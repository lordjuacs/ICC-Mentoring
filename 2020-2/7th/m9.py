matriz = [['P', 'O' ,'P', 'B'], ['E', '4' ,'E', '2'],
          ['R', 'R', 'T', '3'], ['I' ,'5', 'F','L'],
          ['C' ,'L', '5' ,'G'], ['A', 'J', '3' ,'0']]

fila = int(input("Ingrese fila: "))
print(''.join(matriz[fila]))
caracter = input("Ingrese caracter: ")
l = []
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == caracter:
            l.append([i, j])
print("Output", end=" ")
for c in l:
    print('(' + str(c[0]) + ',' + str(c[1]) + ')', end=" ")