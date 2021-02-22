piso1 = 20
piso2 = 20
piso3 = 20
por_piso = 0
for i in range(1, 4):
    por_piso = 0
    print("ingrese datos piso_" + str(i))
    for j in range(1, 5):
        while True:
            ocu = int(input("ingrese las camas ocupadas para la sala_" + str(j) + ":> "))
            if ocu <= 5:
                por_piso += ocu
                break
    if i == 1:
        piso1 -= por_piso
    elif i == 2:
        piso2 -= por_piso
    else:
        piso3 -= por_piso

print("Resultados:")
print("la cantidad de camas disponibles en el piso_1:", piso1)
print("la cantidad de camas disponibles en el piso_2:", piso2)
print("la cantidad de camas disponibles en el piso_3:", piso3)