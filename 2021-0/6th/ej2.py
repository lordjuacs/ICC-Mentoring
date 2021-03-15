file = open("libros.txt", "r")
lines = file.readlines()
lines = lines[1:]
dic = {}
for line in lines:
    (isbn, aut, tit, idi, pub) = line.split(", ")
    dic[isbn] = [aut, tit, idi, int(pub)]
file.close()

filtrar = {}
for isbn in dic:
    if dic[isbn][2] == "Spanish" and dic[isbn][3] < 2016:
        filtrar[isbn] = dic[isbn][0]
file = open("menor-cuantia.txt", "w")
file.write("ISBN Autor\n")
for isbn in filtrar:
    file.write(isbn + ", " + filtrar[isbn] + "\n")
file.close()