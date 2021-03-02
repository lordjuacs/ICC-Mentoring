cadena = input("Texto: ")
par = ""
impar = ""
"""
for i in range(0, len(cadena)):
    if i%2==0:
        par += cadena[i]
    else:
        impar += cadena[i]
"""
orden = 0
for letra in cadena:
    if orden%2==0:
        par += letra
    else:
        impar += letra
    orden += 1
print("Par:", par)
print("Impar:", impar)