string = input('enter your string: ')
x = 0
for i in string:
    if (i.isspace()) == True:
        x += 1
if x > 0:
    print("found ", x+1, "words")
else:
    print("not found")
