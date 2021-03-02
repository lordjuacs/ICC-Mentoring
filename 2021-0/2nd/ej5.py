n = int(input("input: "))
while n <= 0:
    n = int(input("input: "))
print("[", end="")
for i in range(1, n + 1):
    if i == n:
        print(n, end="")
    elif n % i == 0:
        print(i, end=", ")

print("]", end="")
