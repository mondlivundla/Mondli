#we need to create an x-y plane for our island map which is centered at our hero's coordinates

characterX = 1 #horizontal, row number
characterY = 1 #vertical, column number

#the island map is a 2D board of 3x3
island_map = [[":  :" for r in range(3)] for c in range(3)]

#then we need our player('Hero') to be the characterPosition
player = characterPosition = ": H :"

#now we have to place our player('Hero') on the map
island_map[characterY][characterX] = player

#now we must print out the player on our island map
while True:
    for i in island_map:
        print("_____ _____ _____")
        print("  ".join(i))
        print("_____ _____ _____")

        #we have to let the player know which keybindings are used to move on the island map
        print()
        print(" Instructions ")
        print("==============")
        print("Directions____________________Primary Key__________________Secondary Key")
        print()
        print("   Up:                             W                            --      ")
        print("   Down:                           S                            --      ")
        print("   Left:                           A                            --      ")
        print("   Right:                          D                            --      ")
        print()
        print("   Quit:                           Q                            --      ")
        print()

        #implementing the movements on the island map
        direction = input().lower()
        if direction == "w":
            island_map[characterY][characterX] = ":  :"
            characterY -= 1 #we subtract 1 from the column number to move the player upwards
            island_map[characterY][characterX] = player

        elif direction == "s":
            island_map[characterY][characterX] = ":  :"
            characterY += 1 #we add 1 to the column number to move the player upwards
            island_map[characterY][characterX] = player

        elif direction == "a":
            island_map[characterY][characterX] = ":  :"
            characterX -= 1 #we subtract 1 from the row number to move the player leftwards
            island_map[characterY][characterX] = player

        elif direction == "d":
            island_map[characterY][characterX] = ":  :"
            characterY += 1 #we add 1 to the row number to move the player to the right
            island_map[characterY][characterX] = player
