cadena = input("input:\n")
salida = ''

for c in cadena:
    if c == 'a':
        salida += 't'
    elif c == 't':
        salida += 'a'
    elif c == 'g':
        salida += 'c'
    else:
        salida += 'g'
print("output:\n" + salida)