matriz = []
n = int(input("n: "))
l = input("letra: ")

for i in range(n):
    lista = []
    for j in range(n):
        if i == j:
            lista.append(l)
        else:
            lista.append("*")
    matriz.append(lista)
for i in range(n):
    for j in range(n):
        print(matriz[i][j], end=" ")
    print()