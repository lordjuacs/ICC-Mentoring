total = int(input("total:"))
while total < 1 or total > 10:
    total = int(input("total:"))

for i in range(1, total + 1):
    nota1 = int(input("nota 1 de alumno" + str(i) + " :"))
    nota2 = int(input("nota 2 de alumno" + str(i) + " :"))
    print("promedio =", (nota1+nota2)/2)