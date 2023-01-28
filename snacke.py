x = int(input("enter a number: "))

if x % 2 == 1:
    y = (x+1)/2
    for i in range(int(y)):
        print("*", end="")
        if i < y-1:
            print("#", end="")
elif x % 2 == 0:
    y = x / 2
    for i in range(int(y)):
        print("*", end="")
        print("#", end="")
