base = int(input("base: "))
exp = int(input("exp: "))
"""
base, exp = input().split(" ")
base = int(base)
exp = int(exp)"""
output = 1
for i in range(exp):
    output *= base
print("OUTPUT:", output)