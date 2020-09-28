#sume los números pares entre 0 y 100
sum = 0
for i in range(0, 101, 2):
    sum += i
print("Suma: ", sum)

sum = 0
num = 0
while num <= 100:
    sum += num
    num += 2
print("Suma: ", sum)

