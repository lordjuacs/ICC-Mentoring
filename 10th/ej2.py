dic = {"PE": 12, "BR": 15, "EU": 18}
with open("test.txt", "w") as writer:
    for key in dic:
        writer.write(key)
        writer.write(" ")
        writer.write(str(dic[key]))
        writer.write("\n")