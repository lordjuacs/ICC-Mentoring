filas = int(input("Filas [mayor a 2]: "))
while filas <= 2:
    filas = int(input("Filas [mayor a 2]: "))

columnas = int(input("Columnas [mayor a 4]: "))
while columnas <= 4:
    columnas = int(input("Columnas [mayor a 4]: "))

for i in range(filas):
    for j in range(columnas):
        if i == 0 or i == filas - 1 or j == 0 or j == columnas - 1:
            print("*", end=" ")
        else:
            print("o", end=" ")
    print()