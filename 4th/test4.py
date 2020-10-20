n = int(input("Ingrese un numero: "))
for i in range(n):
    print(i + 1, end=" ")
    for j in range(n):
        if i >= j:
            if i%2 != 0:
                if j%2 != 0:
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                if j%2 == 0:
                    print("*", end="")
                else:
                    print(" ", end="")

    print()
