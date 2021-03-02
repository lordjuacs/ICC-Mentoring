file = input("Ingrese el nombre del archivo: ")
#f = open(file, "r")
with open(file, "r") as reader:
  r = reader.readlines()
  for i in r:
    print(i)
"""
dic = {}
for line in f:
  (pais, indice) = line.split(" ")
  dic[pais] = float(indice)

print(sum(list(dic.values()))/len(dic))
f.close()
"""

