"""
n = int(input())
suma = 0
for i in range(1, n+1):
    suma += 1/(i*(i+1))
print(round(suma, 4))


dis = 1500
while True:
    mi = int(input())
    sec = int(input())
    if mi == 0:
        break
    print(round(dis/((mi*60)+sec),4))

"""
"""
n = int(input())
suma = 0
cont = 0
for i in range(-n, n+1):
    for j in range(-n, n+1):
        suma = i + j
        if(suma == 0):
            cont +=1
print(cont)
"""