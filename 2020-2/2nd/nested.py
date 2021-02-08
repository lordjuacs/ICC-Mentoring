n = 5
m = 5
print("  ", end="")
for j in range(m):
    print(j, end=" ")
print()
for i in range(n):
    print(i, end=" ")
    for j in range(m):
        if i == 0 or i == n-1 or i == j:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
