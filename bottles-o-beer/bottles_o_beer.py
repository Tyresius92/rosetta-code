num = 99
no = "No more"
one_bottle = " bottle of beer"
bottles = " bottles of beer"
wall = " on the wall"
take = "Take one down, pass it around"

while num > 0:
    print(str(num) + bottles + wall)
    print(str(num) + bottles)
    print(take)
    num -= 1
    if num == 1:
        print(str(num) + one_bottle + wall + '\n')
    elif num == 0:
        print(no + bottles + wall + '\n')
    else:
        print(str(num) + bottles + wall + '\n')

print(no + bottles + wall)
print(no + bottles)
print("Go to the store and buy some more")
print("99" + bottles + wall + "!")
