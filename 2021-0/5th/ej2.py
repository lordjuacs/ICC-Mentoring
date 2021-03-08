reniec = {"10345678": "Jaime",
          "23456789": "Pedro",
          "46732212": "Carlos",
          "76554434": "Macarena",
          "34567890": "Julia",
          "67554875": "Pedro",
          "76543321": "Julia",
          "76765432": "Carlos",
          "87654323": "Pedro"
          }

ordenados = sorted(list(reniec.keys()))
print("Ordenados por DNI")
for dni in ordenados:
    print(dni, end="\t")
    print(reniec[dni])


def bus_dni():
    dni = input("DNI a buscar: ")
    if dni in reniec.keys():
        print("El nombre asociado es", reniec[dni])
    else:
        print("No hay registro")


bus_dni()


def bus_persona():
    persona = input("Nombre: ")
    dnis = []
    for key in reniec:
        if reniec[key] == persona:
            dnis.append(key)
    print(dnis)


bus_persona()
