file = open("datos.txt", "r")
lines = file.readlines()
print(lines)
dic = {}
for line in lines:
    (key, value) = line.split(" ")
    dic[key] = float(value)

file.close()
print(dic)
print("avg: ", sum(list(dic.values()))/len(dic))