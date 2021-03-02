temp = [[17, 18, 16, 20, 18],
        [7, 5, 6, 6, 7],
        [15, 14, 16, 14, 15],
        [22, 23, 21, 22, 24],
        [1, -5, -1, 0, -2]]
proms = []
suma = 0
for i in range(len(temp)):
    suma = 0
    for j in range(len(temp[0])):
        suma += temp[i][j]
    proms.append(suma / len(temp[0]))
alta = 0
ialta = 0
for i in range(len(temp)):
    if max(temp[i]) > alta:
        alta = max(temp[i])
        ialta = i
baja = 0
ibaja = 0
for i in range(len(temp)):
    if min(temp[i]) < baja:
        baja = min(temp[i])
        ibaja = i

dic = {0: "Lima", 1: "Cusco", 2: "Tacna",
       3: "Trujillo", 4: "Puno"}
for i in range(len(temp)):
    print(dic[i], proms[i])
print("Temp mas alta:", dic[ialta], alta)
print("Temp mas baja:", dic[ibaja], baja)
