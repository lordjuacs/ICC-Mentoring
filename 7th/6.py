def conversion(n = 8):
    lista = []
    while (n >= 1):
        lista.append(n % 2)
        n //= 2
    return lista

n = input("Input: conversion ")
if n == "":
    rpta = conversion() # rpta = lista
    print("Output:", rpta)
elif int(n) < 0 or int(n) > 8:
    print("Por favor intentelo de nuevo")
else:
    n = int(n)
    rpta = conversion(n)
    print("Output:", rpta)


