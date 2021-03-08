alumnos = {"Alejandro": ["ceviche", "lomo saltado", "pollo a la brasa"],
           "Roberto": ["lomo saltado"],
           "Jesus": ["lomo saltado", "lasagna"],
           "Carlos": ["lasagna"],
           "Melina": ["ceviche", "arroz con pollo"]}

comparten = {}
for persona in alumnos:
    for comida in alumnos[persona]:
        if comparten.get(comida) is not None:
            comparten[comida].append(persona)
        else:
            comparten[comida] = [persona]

for comida in comparten:
    if len(comparten[comida]) > 1:
        for i in range(len(comparten[comida])):
            print(comparten[comida][i], end=" ")
            if i == len(comparten[comida]) - 1:
                break
            if i == len(comparten[comida]) - 2:
                print("y", end=" ")
            else:
                print(",", end=" ")
        print()
