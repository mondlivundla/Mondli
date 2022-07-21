"""
We are to develop a RockPaperScissors game which is text based
"""
#import random module in order to generate random values in our game
import random
from tkinter import END

#We are to welcome a user to our RockPaperScissors game
print("   Welcome to our text based 'RockPaperScissors' game  ")
print("=======================================================")#the string of equal signs printed are supposed to act as an underline

#Now we ask the user if he/she wishes to play the game
answer = input("Do you wish to play 'RockPaperScissors' against the computer? ").lower() #the (.lower) makes the values input by the user to remain lowcase

if answer == "yes" or "y":
    print(" Okay Great!!!!!! ")
else:
    print(" Goodbye my friend! ")
    quit()#if the statement is false then the program is supposed to exit on the spot

#then we have to give the player a username
username = input(" Please enter your preferred username to proceed: ")

if username: #while username is true print the statement below
    print("Okay " + str(username) + " let's play!!!")
    pass
else:
    print("Please enter a username")

#the initial number of wins at the beginning of the game is always at zero for both players
COM_user_wins = 0
username_wins = 0

#Our game has three available choices which can be identified if 'choices' is made a tuple
choices = ["rock", "paper", "scissors"]
         #[  0,       1,         2    ]

play = random.randint(0, 2)

while True:
    computer_pick = choices[play] # thecomputer has to randomly pick, so we have to generate a random value and use it as the index point of the tuple 'choices' 
    user_pick = input("Pick your choice, 'rock/paper/scissors'")

    if user_pick == ("rock" or "r") and computer_pick == "scissors":
        print(str(username) + " picked " + str(user_pick))
        print("Computer picked " + str(computer_pick))
        print(str(username) + " wins")
        print("_______________________")
        username_wins += 1#add one mark if the player wins

    elif user_pick == ("paper" or "p") and computer_pick == "rock":
        print(str(username) + " picked " + str(user_pick))
        print("Computer picked " + str(computer_pick))
        print(str(username) + " wins")
        print("_______________________")
        username_wins += 1

    elif user_pick == ("scissors" or "s") and computer_pick == "paper":
        print(str(username) + " picked " + str(user_pick))
        print("Computer picked " + str(computer_pick))
        print(str(username) + " wins")
        print("_______________________")
        username_wins += 1

    else:
        print("Computer wins")
        COM_user_wins += 1
        break#loop stops when the computer wins

print("You won " + str(username_wins) + " times.")
print("The computer won " + str(COM_user_wins) + " times.")
END#end of the program


