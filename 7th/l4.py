l1 = input("A: ")
l2 = input("B: ")
l1 = l1.split(",")
l2 = l2.split(",")
inter = 0
union = len(l1)
for x in l2:
    if x in l1:
        inter +=1
    if x not in l1:
        union += 1

print("Interseccion:", inter)
print("Union:", union)
print("Jaccard", round(inter/union, 2))
