"""
def invertir(lista):
    out = []
    for i in range(len(lista) - 1, -1, -1):
        out.append(lista[i])
    return out
lista = [0, 1, 2, 3, 4]
#lista2 = [4, 3, 2, 1]
lista2 = invertir(lista)
print(lista2)
"""
def fibonacci(index):
    if index == 0 or index == 1:
        return 1
    return fibonacci(index - 1) + fibonacci(index - 2)

def lista_fibonacci(n = 10):
    lista = []
    for i in range(n):
        lista.append(fibonacci(i))
    return lista
#n = int(input("Ingrese n: "))

#index       0  1  2  3  4  5
# n = 5 --> [1, 1, 2, 3, 5, 8 ...]
fibo = lista_fibonacci()
print(fibo)