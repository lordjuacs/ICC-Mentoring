import random
def desordenar(lista):
    a = 0
    b = len(lista) - 1
    for i in range(len(lista)):
        temp = lista[i]
        otro_pos = random.randint(a,b)
        lista[i] = lista[otro_pos]
        lista[otro_pos] = temp

    return lista


lista = []
for i in range(10):
    lista.append(float(input("Ingrese valor para la lista: ")))
#print("Lista:", lista)
#print("Lista deordenada:", desordenar(lista))
print("Lista:", end=" ")
for i in range(len(lista)):
    if i == len(lista) - 1:
        print(lista[i], end="")
    else:
        print(lista[i], end=",")
print()

lista = desordenar(lista)
print("Lista desordenada:", end=" ")
for i in range(len(lista)):
    if i == len(lista) - 1:
        print(lista[i], end="")
    else:
        print(lista[i], end=",")
print()