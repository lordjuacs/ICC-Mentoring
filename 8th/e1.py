frase1 = input("Ingrese frase1: ")
frase2 = input("Ingrese frase2: ")
while len(frase1) != len(frase2):
    frase1 = input("Ingrese frase1: ")
    frase2 = input("Ingrese frase2: ")
voc1 = 0
voc2 = 0
cons1 = 0
cons2 = 0


for i in range(len(frase1)):
    if frase1[i].lower() in ['a', 'e', 'i', 'o', 'u']:
        voc1 += 1
    elif ord(frase1[i].lower()) in range(97, 123):
        cons1 += 1
    if frase2[i].lower() in ['a', 'e', 'i', 'o', 'u']:
        voc2 += 1
    elif ord(frase2[i].lower()) in range(97, 123):
        cons2 += 1

otro1 = len(frase1) - voc1 - cons1
otro2 = len(frase2) - voc2 - cons2

if otro1 > otro2:
    inversa = frase1[::-1]
    #inversa = ""
    #for c in frase1:
    #    inversa = c + inversa
else:
    inversa = frase2[::-1]
print("Vocales frase 1=", voc1, "frase2=", voc2)
print("Consonantes frase 1=", cons1, "frase2=", cons2)
print("Otros caracteres frase 1=", otro1, "frase2=", otro2)
print("Frase invertida:", inversa)
