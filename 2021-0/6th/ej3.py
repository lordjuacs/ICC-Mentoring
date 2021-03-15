from random import *

lista = [randint(1, 100) for i in range(10)]
print(lista)
lista2 = [x ** 2 for x in lista]
print(lista2)
lista3 = lista + lista2
print(lista3)
count = 1
while count <= 4:
    lista3.remove(min(lista3))
    count += 1
print(lista3)
count = 0
for num in lista3:
    print(num, end=" ")
    count += 1
    if count == 4:
        print()
        count = 0
