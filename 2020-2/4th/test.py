n = int(input("Ingrese un numero: "))

for j in range(0, n):
    cont = 1
    for i in range(1, n - j):
        print(" ", end="")
    if j == 0:
        print(j + 1, end="")
    else:        
        for i in range(1, j + 1):
            print(cont, end="")
            cont += 1
        print(" ", end="")
        cont -= 1
        for i in range(1, j + 1):
            print(cont, end="")
            cont -= 1
    for i in range(1, n - j):
        print(" ", end="")
    print()