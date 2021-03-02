n = int(input("Ingrese el total de numeros:"))
while n <= 0:
    n = int(input("Ingrese el total de numeros:"))

maximo = -999999
minimo = 999999
for i in range(0, n):
    num = int(input("Numero:"))
        #47 > 69
    if num > maximo:
        maximo = num
        #maximo = 69

        #47 < 10
    if num < minimo:
        minimo = num
        #minimo = 10
print("Maximo:", maximo, "Minimo:", minimo)