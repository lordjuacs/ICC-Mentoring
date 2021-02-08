distancia = 1500
minutos = int(input("Ingrese los minutos:"))
segundos = int(input("Ingrese los segundos:"))
while minutos != 0:
    velocidad = distancia/((minutos * 60) + segundos)
    print("velocidad:", round(velocidad, 4), "metros/s")
    minutos = int(input("Ingrese los minutos:"))
    segundos = int(input("Ingrese los segundos:"))
