n = int(input("Ingrese un numero: "))

if n % 2 == 0 and n > 20:
    print("es par y grande")
elif n % 2 == 0 and n < 0:
    print("Es par y negativo")
elif n % 2 == 0:
    print("es par")
else:
    print("Es impar")
