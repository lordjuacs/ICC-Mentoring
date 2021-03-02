import math
def siguientecuadrado(n):
    if math.sqrt(n).is_integer():
        return int(math.sqrt(n))
    return int(math.ceil(math.sqrt(n)))

texto = input("Ingrese texto")
m = siguientecuadrado(len(texto))
matriz = []
cont = 0
for i in range(m):
    lista = []
    for j in range(m):
        if cont < len(texto):
            lista.append(texto[cont])
            cont +=1
        else:
            lista.append('@')
    matriz.append(lista)



for lista in matriz:
    print(lista)