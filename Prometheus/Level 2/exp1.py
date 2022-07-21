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

#treasures
treasure1 = {
    'Name': 'Treasure1',
    'XP': 20
    }
treasure2 = {
    'Name': 'Treasure2',
    'XP': 20
    }

#random coordinates
wolfX = random.randint(0, 2)
wolfY = random.randint(0, 2) 
fireX = random.randint(0, 2)
fireY = random.randint(0, 2)
treasure1X = 1
treasure1Y = 2
treasure2X = 2
treasure2Y = 0


#then we need a symbol or representation of our player(Hero), for wolf
player = ": H :"
wolf = ": W :"
fire = ": F :"
treasure1 = ": T1 :"
treasure2 = ": T2 :"
#then we need to create a board for our game
island_map = [
    [":  :" for r in range(3)]
     for c in range(3)
    ]

#Now we have to place our player or characterPosition on the board
def char_coordinates():
    global island_map
    global characterX
    global characterY
    island_map[characterY][characterX] = player

    #place treasures on the island map
    def treasure():
        global island_map
        island_map[treasure1Y][treasure1X] = treasure1
        island_map[treasure2Y][treasure2X] = treasure2
    treasure()
    #place wolf on the island map
    def wolf_coord():
        global island_map
        global wolfY
        global wolfX
        global treasure1X
        global treasure1Y
        global treasure2X
        global treasure2Y
        global characterX
        global characterY
        if wolfX == 1 and wolfY == int(1):#if the coordinates of the wolf clashes with the coordinates of the player(hero) then start a loop
            wolfX = random.randint(0,2)
            
        elif wolfX == treasure1X and wolfY == treasure1Y:
            wolfX = random.randint(0, 2)
            wolfY = random.randint(0, 2)
        elif wolfX == treasure2X and wolfY == treasure2Y:
            wolfX = random.randint(0, 2)
            wolfY = random.randint(0, 2)
        else:
            island_map[wolfX][wolfY] = wolf
    wolf_coord()
    #place fire on the island map
    def fire_coord():
        global island_map
        global wolfY
        global wolfX
        global fireX
        global fireY
        global treasure1X
        global treasure1Y
        global treasure2X
        global treasure2Y
        if fireY == 1 and fireX == 1:#if the coordinates of the fire clash with the player(hero) then start a loop
            fireX = random.randint(0, 2)
            fireY = random.randint(0, 2)
        elif fireY == wolfY and fireX == wolfX:#also if the coordinates of fire clash with the wolf, start a loop
            fireX = random.randint(0, 2)
            fireY = random.randint(0, 2)
        elif fireY == treasure1Y and fireX == treasure1X:
            fireX = random.randint(0, 2)
            fireY = random.randint(0, 2)
        elif fireY == treasure2Y and fireX == treasure2X:
            fireX = random.randint(0, 2)
            fireY = random.randint(0, 2)
        else:
            island_map[fireY][fireX] = fire
    fire_coord()

    
char_coordinates()
while True:
    for u in island_map:
        print("_____   _____   _____")
        print(":  :".join(u))
        print("_____   _____   _____")
        

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
        if player == island_map[wolfY][wolfX]:
            print("WOLFFFFFF!!!!!")
            while True:
                answer = input("Do you wish to fight or run?\n 1.fight\n 2.run\n action: ").lower().strip()
                if answer == "fight":
                    player.update({'XP': 20})
                    print(player.get({'XP'}))
        print("Location: ", characterX, ",", characterY)
        if True:
            if characterY == 0 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 1 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 2 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 0:
                print("out of range")
                characterY -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 1:
                print("out of range")
                characterY -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 2:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            
                

    elif direction == "s":
        island_map[characterY][characterX] = ":  :"
        characterY += 1#we add 1 to the column number to move downwards
        island_map[characterY][characterX] = player
        if player == wolfY and wolfY:
            print("WOLFFFFFF!!!!!")
            while True:
                answer = input("Do you wish to fight or run?\n 1.fight\n 2.run\n action: ").lower().strip()
                if answer == "fight":
                    player.update({'XP': 20})
                    print(player.get({'XP'}))
        print("Location: ", characterX,",", characterY)
        if True:
            if characterY == 0 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 1 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 2 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 0:
                print("out of range")
                characterY -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 1:
                print("out of range")
                characterY -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 2:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            

    elif direction == "a":
        island_map[characterY][characterX] = ":  :"
        characterX -= 1#we subtract 1 from the row number to move leftwards
        island_map[characterY][characterX] = player
        if player == wolfY and wolfY:
            print("WOLFFFFFF!!!!!")
            while True:
                answer = input("Do you wish to fight or run?\n 1.fight\n 2.run\n action: ").lower().strip()
                if answer == "fight":
                    player.update({'XP': 20})
                    print(player.get({'XP'}))
        print("Location: ", characterX, ",", characterY)
        if True:
            if characterY == 0 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 1 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 2 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 0:
                print("out of range")
                characterY -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 1:
                print("out of range")
                characterY -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 2:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            

    elif direction == "d":
        island_map[characterY][characterX] = ":  :"
        characterX += 1#we add 1 to the row number to move rightwards
        island_map[characterY][characterX] = player
        if player == wolfY and wolfY:
            print("WOLFFFFFF!!!!!")
            while True:
                answer = input("Do you wish to fight or run?\n 1.fight\n 2.run\n action: ").lower().strip()
                if answer == "fight":
                    player.update({'XP': 20})
                    print(player.get({'XP'}))
        print("Location: ", characterX, ",", characterY)
        if True:
            if characterY == 0 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 1 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 2 and characterX == 3:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 0:
                print("out of range")
                characterY -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 1:
                print("out of range")
                characterY -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            elif characterY == 3 and characterX == 2:
                print("out of range")
                characterX -= 1
                island_map[characterY][characterX] = player
                print("Location: ", characterX, characterY)
            
            

    elif direction == "q":#make an exit button available throughout
        quit()
        END
