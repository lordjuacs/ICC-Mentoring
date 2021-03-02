#personas = {"Luis": [20, 14], "Carlos": [18, 15], "Carmen": [15, 20]}
#personas.clear()
#for i in personas:
#    print(i, sum(personas[i])/len(personas[i]))
# string = input("Input: ")
# unicos = []
# for a in string:
#     if a.lower() not in unicos and a != ' ':
#         unicos.append(a.lower())
# dic = {}
# for a in unicos:
#     dic[a] = string.lower().count(a)
# print("Ouput", dic)
def contar(lista):
    unicos = []
    for i in lista:
        if i not in unicos:
            unicos.append(i)
    dic = {}
    for a in unicos:
        dic[a] = lista.count(a)
    return dic

lista = input("Ingrese la lista de decimales: ").replace("[", "").replace("]", "").split(", ")
lista = [float(x) for x in lista]
dic = contar(lista)
for a in dic:
    print(a, "=", dic[a])
