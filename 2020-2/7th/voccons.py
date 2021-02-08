parrafo = "o sea las palabras que empiezan por vocales en una lista y las que empiezan en consonantes"
lista = parrafo.split(" ")
vocales = []
consonantes = []
for palabra in lista:
    if palabra[0].lower() in ['a', 'e','i', 'o', 'u']:
        vocales.append(palabra)
    else:
        consonantes.append(palabra)
print("vocales:", vocales)
print("consonantes:", consonantes)