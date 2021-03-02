alumnos = {"Alejandro": ["ceviche", "lomo saltado", "pollo a la brasa"],
           "Roberto": ["lomo saltado"],
           "Jesus": ["lomo saltado", "lasagna"],
           "Carlos": ["lasagna"],
           "Melina": ["ceviche", "arroz con pollo"]}

comparten = {}
for key in alumnos:
    for comida in alumnos[key]:
        if comparten.get(comida) is not None:
            comparten[comida].append(key)
        else:
            comparten[comida] = [key]

for key in comparten:
    if len(comparten[key]) > 1:
        for i in range(len(comparten[key])):
            print(comparten[key][i], end=" ")
            if i == len(comparten[key]) - 1:
                break
            if i == len(comparten[key]) - 2:
                print("y", end=" ")
            else:
                print(",", end=" ")
        print()

