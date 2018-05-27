OPEN = "Open"
CLOSED = "Closed"

door_list = []

for i in range(1, 100):
    door_list.append(CLOSED)

for i in range(len(door_list)):
    print(str(i) + ": " + door_list[i])

for mod in range(1, 100):
    for door in range(0, 99):
        if door % mod == 0:
            if door_list[door] == OPEN:
                door_list[door] = CLOSED
            else:
                door_list[door] = OPEN


for i in range(len(door_list)):
    print(str(i) + ": " + door_list[i])
