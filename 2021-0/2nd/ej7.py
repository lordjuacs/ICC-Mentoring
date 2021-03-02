#2(i^2)
n = int(input("n: "))
while n <= 0:
    n = int(input("n: "))
suma = 0
i = 1
while True:
    suma += 2 * (i**2)
    i += 1
    if i == n + 1:
        break
print(suma)
