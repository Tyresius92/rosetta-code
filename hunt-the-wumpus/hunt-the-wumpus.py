import random

WUMPUS_MSG = "You smell something terrible nearby."
BAT_MSG = "You hear a rustling."
PIT_MSG = "You feel a cold wind blowing from a nearby cavern."

PIT = "pit"
WUMPUS = "wumpus"
BAT = "bat"
PLAYER = "player"

SHOOT = 's'
ENTER = 'e'
QUIT = 'q'

def populate_rooms():
    rooms = []

    for i in range(20):
        rooms.append(None)

    for i in range(2):
        pit_rm = get_empty_room(rooms)
        rooms[pit_rm] = PIT

    for i in range(2):
        bat_rm = get_empty_room(rooms)
        rooms[bat_rm] = BAT

    wumpus_rm = get_empty_room(rooms)
    rooms[wumpus_rm] = WUMPUS

    player_rm = get_empty_room(rooms)
    rooms[player_rm] = PLAYER

    return rooms

def get_empty_room(rooms):
    while True: 
        room_num = random.randint(0, 19)
        if rooms[room_num] == None:
            break
    return room_num

def print_turn_msgs():
    msg_printed = False
    player_rm = rooms.index(PLAYER)
    
    for connect in room_connections[player_rm]:
        if rooms[connect] == WUMPUS:
            print(WUMPUS_MSG)
            msg_printed = True
        elif rooms[connect] == BAT:
            print(BAT_MSG)
            msg_printed = True
        elif rooms[connect] == PIT:
            print(PIT_MSG)
            msg_printed = True

    if msg_printed == False:
        print("It is eerily silent. You sense nothing nearby.")

    print("You have " + str(num_arrows) + " arrows remaining.")

def get_player_action():
    print("Would you like to shoot, or enter another room?")
    print("Enter s to shoot, or e to go to another room.")

    while True:
        action = input().lower()
        if action in [SHOOT, ENTER, QUIT]:
            break
        else:
            print("That is not a valid input.")
            print("Please enter s to shoot, e to go to another room.")
            print("You may also enter q to quit.")

    return action

def get_player_room_choice(action):
    print("Would you like to ", end='')
    if action == SHOOT:
        print("shoot ", end='')
    elif action == ENTER:
        print("go ", end='')
    print("into room 1, 2, or 3?")

    while True:
        room_choice = input()
        if room_choice in ['1', '2', '3']:
            break
        else:
            print("That is not a valid room number.")
            print("Please enter 1, 2, or 3.")

    return int(room_choice)

room_connections = [ [ 7, 13, 9 ],
                     [ 12, 18, 0 ],
                     [ 16, 17, 19 ],
                     [ 11, 14, 18 ],
                     [ 13, 15, 18 ],
                     [ 9, 14, 16 ],
                     [ 1, 15, 17 ],
                     [ 10, 16, 0 ],
                     [ 6, 11, 19 ],
                     [ 8, 12, 17 ],
                     [ 4, 13, 9 ],
                     [ 2, 10, 15 ],
                     [ 1, 5, 11 ],
                     [ 4, 6, 0 ],
                     [ 5, 7, 12 ],
                     [ 3, 6, 8 ],
                     [ 3, 7, 10 ],
                     [ 2, 4, 5 ],
                     [ 1, 3, 9 ],
                     [ 2, 8, 14 ] ]

rooms = populate_rooms()

num_arrows = 5
game_over = False
play_again = True

print("Welcome to Hunt the Wumpus!")

while not game_over:
    print_turn_msgs()
    
    action = get_player_action()
    

    if action == QUIT:
        game_over = True
        print("Thank you for playing Hunt the Wumpus!")
        print("Have a great day!")

    room_choice = get_player_room_choice(action)
    if action == SHOOT:
        

        
    if action == ENTER:
        enter_room(room_choice)


