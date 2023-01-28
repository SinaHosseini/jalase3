x = int(input("enter tol arraye: "))

tartib = True

list = []

for i in range(x):
    list.append(int(input("enter your number: ")))

print(list)

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            tartib = False

print(list)

if tartib == False:
    print("not orgnize")
else:
    print("orgnize")
