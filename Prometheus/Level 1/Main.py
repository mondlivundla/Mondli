#Before creating a board we need coordinates, infact we need a an x-y plane for a 2D board
from tkinter import END
import random

characterX = 1 #horizontal, row number
characterY = 1 #vertical, column number

#our player(Hero)
player = {
    'Name': 'Hero',
    'XP': 50,
    'characterX': 1,
    'characterY': 1
    }

#wolf
animal = {
    'Name': 'Wolf',
    'XP': 30
    }

#fire
fire = {
    'Name': 'Fire',
    'XP': 25}

#random coordinates
wolfX = random.randint(0, 2)
wolfY = random.randint(0, 2)
fireX = random.randint(0, 2)
fireY = random.randint(0, 2)
if wolfY == int(1) and wolfX == int(1):  #if the coordinates of the wolf clashes with the coordinates of the player(hero) then start a loop
    wolfX = random.randint(0,2)
    wolfY = random.randint(0,2)
if (fireY and fireX == 1):#if the coordinates of the fire clash with the player(hero) then start a loop
    fireX = random.randint(0, 2)
    fireY = random.randint(0, 2)
    if fireX == str(wolfX) and fireX == str(wolfY):#also if the coordinates of fire clash with the wolf, start a loop
        fireX = random.randint(0, 2)
        fireY = random.randint(0, 2)
#then we need a symbol or representation of our player(Hero), for wolf
player = ": H :"
wolf = ": W :"
fire = ": F :"
#then we need to create a board for our game
island_map = [
    [":  :" for r in range(3)]
     for c in range(3)
    ]

#Now we have to place our player or characterPosition on the board
if True:
    island_map[characterY][characterX] = player
    #place wolf on the island map
    island_map[wolfY][wolfX] = wolf
    #place fire on the island map
    island_map[fireX][fireY] = fire

while True:
    for u in island_map:
        print("_____ _____ _____")
        print(": :".join(u))
        print("_____ _____ _____")
        

    #We have to let the user know which keybindings are used in the game
    print("                        Instructions                              ")
    print("                      ================                            ")
    print("Directions_______________Primary Key_______________________Secondary Key")
    print("Up:                          W                                  --") #moving up the vertical axis
    print("Down:                        S                                  --") #moving down the vertical axis
    print("Left:                        A                                  --") #moving to the left on the horizontal axis
    print("Right:                       D                                  --") #moving to the right on the horizontal axis
    print()
    print("Quit: Q") #to exit you press q-key
    print()
    #implementing the directions practically
    direction = input("Please start moving: ").lower().strip()
    if direction == "w":
        island_map[characterY][characterX] = ":  :"
        characterY -= 1#we subtract 1 from the column number to move upwards
        island_map[characterY][characterX] = player

    elif direction == "s":
        island_map[characterY][characterX] = ":  :"
        characterY += 1#we add 1 to the column number to move downwards
        island_map[characterY][characterX] = player

    elif direction == "a":
        island_map[characterY][characterX] = ":  :"
        characterX -= 1#we subtract 1 from the row number to move leftwards
        island_map[characterY][characterX] = player

    elif direction == "d":
        island_map[characterY][characterX] = ":  :"
        characterX += 1#we add 1 to the row number to move rightwards
        island_map[characterY][characterX] = player

    elif direction == "q":#make an exit button available throughout
        quit()
        END

    

    





