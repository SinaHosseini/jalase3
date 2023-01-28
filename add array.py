import random
x = int(input("enter tol arraye: "))

list = []

for i in range(x):
    y = random.randint(-100, 100)
    if y in list:
        # print("this number already exist")
        # print("try again!")
        while True:
            y = random.randint
            if y in list:
                print("")
                # print("this number already exist")
                # print("try again!")
            else:
                list.append(y)
                break
    else:
        list.append(y)


print(list)
