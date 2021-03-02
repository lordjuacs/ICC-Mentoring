n = int(input("Ingrese n: "))

for i in range(1, n + 1):
    for j in range(1, i):
        if i % j == 0 and i != j:
            for k in range(1, n + 1):
                if i % k == 0 and i != k and j != k:
                    print("(", i, j, k, ")")

