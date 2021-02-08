while True:
    n = int(input("Ingrese el valor de N: "))
    if n >= 5 and n <= 10:
        break

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n -1 or i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
