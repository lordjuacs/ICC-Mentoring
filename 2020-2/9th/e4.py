def indice_valor(dic, indice):
    return list(dic.keys())[list(dic.values()).index(indice)]

def valor_indice(dic, valor):
    if valor.capitalize() in list(dic.keys()):
        return dic[valor.capitalize()]
    return None



planetas = "Sol@planeta$Mercurio@planeta$Venus@planeta$Tierra@planeta$Marte@planeta$Jupyter@planeta$Saturno@planeta$Urano@planeta$Neptuno@planeta$Pluton"
planetas = planetas.split("@planeta$")
cont = 1
dic = {}
for i in planetas:
    dic[i] = cont
    cont += 1

while True:
    op = int(input("Ingrese una llave desde 1 hasta 10: "))
    if op >= 1 and op <= 10:
        print("El valor con llave", op, "es", indice_valor(dic, op))
        break
while True:
    op = input("Ingrese el nombre de un planeta: ")
    rpta = valor_indice(dic, op)
    if rpta != None:
        print("El valor con llave", op, "es", rpta)
        break