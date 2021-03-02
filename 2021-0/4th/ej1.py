l1 = input().split(",")
l2 = input().split(",")
comun = []
for p in l1:
    if p in l2:
        comun.append(p)
p = sorted(comun)
l = [9, 8, 7, 6, 5, 4]
print(sorted(l))
print(p)
print(comun)
