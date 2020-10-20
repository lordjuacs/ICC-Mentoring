"""while True:
    n = int(input("n:"))
    if n > 0:
        break
"""
n = int(input("n:"))
while n <= 0:
    n = int(input("n:"))
suma = 0
i = 1
while i <= n:
    suma += 1/(i*(i+1))
    i +=1
print(round(suma, 4))