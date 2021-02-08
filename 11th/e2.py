from random import *
with open("numeros.txt", "w") as writer:
    for i in range(20):
        writer.write(str(randint(1, 99)) + "\n")