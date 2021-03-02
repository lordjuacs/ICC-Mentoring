n = int(input("n="))
cont = 0
"""
for i in range(-n, n + 1):
    for j in range(-n, n + 1):
        suma = i + j
        if suma == 0:
            cont += 1
print("Son", cont, "combinaciones igual a 0")
"""
i = -n
while i <= n:
    j = -n
    while j <= n:
        suma = i + j
        if suma == 0:
            cont += 1
        j +=1
    i +=1
print("Son", cont, "combinaciones igual a 0")