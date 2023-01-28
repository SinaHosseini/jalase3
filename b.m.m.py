a = int(input("enter first number: "))
b = int(input("enter second number: "))

if a < b:
    d = a
elif b < a:
    d = b

c = d

for i in range(d):
    if a % c == 0 and b % c == 0:
        break
    else:
        c -= 1


print("b.m.m is: ", c)
