#Before creating a board we need coordinates, infact we need a an x-y plane for a 2D board
from tkinter import END


characterX = 1 #horizontal, row number
characterY = 1 #vertical, column number

#then we need a player or the characterPosition
player = ": H :"

#then we need to create a board for our game
board = [[":  :" for r in range(3)] for c in range(3)]

#Now we have to place our player or characterPosition on the board
board[characterY][characterX] = player

while True:
    for i in board:
        print("_____ _____ _____")
        print("  ".join(i))
        print("_____ _____ _____")

    #We have to let the user know which keybindings are used in the game
    print(" Instructions ")
    print("Directions_______________Primary Key_______________________Secondary Key")
    print("Up:                          W                                  --") #moving up the vertical axis
    print("Down:                        S                                  --") #moving down the vertical axis
    print("Left:                        A                                  --") #moving to the left on the horizontal axis
    print("Right:                       D                                  --") #moving to the right on the horizontal axis
    print()
    print("Quit: Q") #to exit you press q-key
    print()
    #implementing the directions practically
    direction = input("Please start moving: ").lower()
    if direction == "w":
        board[characterY][characterX] = ":  :"
        characterY -= 1#we subtract 1 from the column number to move upwards
        board[characterY][characterX] = player

    elif direction == "s":
        board[characterY][characterX] = ":  :"
        characterY += 1#we add 1 to the column number to move downwards
        board[characterY][characterX] = player

    elif direction == "a":
        board[characterY][characterX] = ":  :"
        characterX -= 1#we subtract 1 from the row number to move leftwards
        board[characterY][characterX] = player

    elif direction == "d":
        board[characterY][characterX] = ":  :"
        characterX += 1#we add 1 to the row number to move rightwards
        board[characterY][characterX] = player

    elif direction == "q":#make an exit button available throughout
        quit()
        END

    elif direction == "ww":#we need to be able to perform double moves
        board[characterY][characterX] = ":  :"
        characterY -= 2#we subtract 2 from the column number to move upwards
        board[characterY][characterX] = player

    elif direction == "ss":#we need to be able to perform double moves
        board[characterY][characterX] = ":  :"
        characterY += 2#we add 2 to the column number to move downwards
        board[characterY][characterX] = player

    elif direction == "aa":#we need to be able to perform double moves
        board[characterY][characterX] = ":  :"
        characterX -= 2#we subtract 2 from the row number to move leftwards
        board[characterY][characterX] = player

    elif direction == "dd": #we need to be able to perform double moves
        board[characterY][characterX] = ":  :"
        characterX += 2#we add 2 to the row number to move rightwards
        board[characterY][characterX] = player

    





