def resta(a, b, c):
    return (a + b) - c


def fun1(a=5, b=10):
    return a / b


def triplica(l):
    l = [3 * l[i] for i in range(len(l))]
    return l


lista = [1, 4, 5]
lista = triplica(lista)
print(lista)


def imprimir(st):
    print(st)


imprimir(input("escriba: "))
