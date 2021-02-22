#ADN
cadena = input("input:")
salida = ""
for letra in cadena:
    if letra.upper() == "A":
        salida += "T"
    elif letra.upper() == "T":
        salida += "A"
    elif letra.upper() == "G":
        salida += "C"
    elif letra.upper() == "C":
        salida += "G"
print("output:")
print(salida)