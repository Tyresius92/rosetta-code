print("Please enter two integers, separated by a space.")

int_list = []

while len(int_list) != 2:
    try:
        [a, b] = input().split()
        a = int(a)
        b = int(b)
        break
    except:
        print("That is not valid input. Please try again.")

sum = a + b

print(sum)
