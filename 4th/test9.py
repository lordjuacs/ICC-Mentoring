cadena = input("Texto: ")
pal = 1
for letra in cadena:
    if letra == " ":
        pal +=1
while pal <= 4:
    cadena = input("Texto: ")
    pal = 1
    for letra in cadena:
        if letra == " ":
            pal += 1
tot = len(cadena) - pal + 1
voc = 0
cons = 0
"""
for letra in cadena:
    if letra != " ":
        if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
            voc += 1
        else:
            cons += 1
"""
for letra in cadena:
    if letra != " ":
        if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
            voc += 1
        elif ord(letra) in range(65, 91) or ord(letra) in range(97, 123):
            cons += 1
print("total de caracteres", tot)
print("total de vocales", voc)
print("total de consonantes", cons)
print("total de espacios", pal - 1)
