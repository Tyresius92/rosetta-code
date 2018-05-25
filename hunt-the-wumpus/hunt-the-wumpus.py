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

    print("You have " + str(num_arrows) + " arrows remaining.\n")

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

    return int(room_choice) - 1

def enter_room(rooms, room_num):
    player_rm = rooms.index(PLAYER)
    goto_rm = room_connections[player_rm][room_num]

    if rooms[goto_rm] == WUMPUS:
        print("You have stumbled into the lair of the Wumpus!")
        print("He leaps on you and gobbles you up!")
        print("You have lost.\n")
        game_over = True
    elif rooms[goto_rm] == PIT:
        print("You enter the room, and fall into a bottomless pit!")
        print("You fall forever.")
        print("You have lost.\n")
        game_over = True
    elif rooms[goto_rm] == BAT:
        print("Upon entering the room, a huge bat grabs you!")
        print("It carries you to a different room.\n")
        rooms[player_rm] = None
        player_rm = get_empty_room(rooms)
        rooms[player_rm] = PLAYER
        game_over = False
    elif rooms[goto_rm] == None:
        print("You enter another room.\n")
        rooms[player_rm] = None
        player_rm = room_connections[player_rm][room_num]
        rooms[player_rm] = PLAYER
        game_over = False

    return game_over

def shoot_room(rooms, room_num, num_arrows):
    player_rm = rooms.index(PLAYER)
    shoot_rm = room_connections[player_rm][room_num]

    if rooms[shoot_rm] == WUMPUS:
        print("You have shot and killed the Wumpus!")
        print("You win!\n")
        game_over = True
    elif rooms[shoot_rm] == PIT:
        print("You shoot into the room and lose an arrow.\n")
        game_over = False
    elif rooms[shoot_rm] == BAT:
        print("You have killed a bat!\n")
        rooms[shoot_rm] = None
        game_over = False
    elif rooms[shoot_rm] == None:
        print("You shoot into the room and lose an arrow.\n")
        game_over = False

    if not game_over:
        num_arrows -= 1

        if (random.randint(1, 4) % 4) == 0:
            wump_rm = rooms.index(WUMPUS)
            rooms[wump_rm] = None
            wump_rm = room_connections[wump_rm][random.randint(0, 2)]
            if (wump_rm == player_rm):
                print("The Wumpus enters the room with you and gobbles you up!")
                print("You have lost.\n")
                game_over == True
            else:
                rooms[wump_rm] = WUMPUS

        elif num_arrows == 0:
            print("You have run out of arrows!")
            print("You have lost.")
            game_over = True

    return game_over, num_arrows

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


game_over = False
play_again = True

while play_again:
    print("Welcome to Hunt the Wumpus!\n")
    rooms = populate_rooms()
    num_arrows = 5
    
    while not game_over:
        print_turn_msgs()
        
        action = get_player_action()

        if action == QUIT:
            game_over = True
            play_again = False
            print("Thank you for playing Hunt the Wumpus!")
            print("Have a great day!")
            break

        room_choice = get_player_room_choice(action)
        if action == SHOOT:
            game_over, num_arrows = shoot_room(rooms, room_choice, num_arrows)
            
        if action == ENTER:
            game_over = enter_room(rooms, room_choice)

    if action != QUIT:
        print("Would you like to play again? [y/n]")
        play_again = input().lower().startswith('y')
        if play_again:
            game_over = False
