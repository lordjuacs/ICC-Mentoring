n = int(input("n: "))
cont = 1
while n:
    bin = 0
    if n%2 == 1:
        bin=1;
    for i in range(bin, cont + bin):
        print(i%2, end="")
    print()
    cont += 1
    n -= 1
