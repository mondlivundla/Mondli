#first thing make it possible to use some functions in this program we have to import a particular built-in function
import random

#Now we have to welcome the player to our number guessing game
print("Hello there, welcome to our number guessing game!")

#Give the player a chance to say the top number of their choice which is equal or greater than 5
print("Please enter an end value of your guess range value which is equal or greater than 5")

#store the top range value as top_number:
top_number = input()
#check if the entered value is a valid number that is <= 5
if top_number.isdigit():
    top_number = int(top_number) > 4
elif top_number.isdigit():
    top_number = float(top_number) > 4
else:
    print("Enter a valid number next time")
    quit() #exit program if player inputs invalid number
random_number = random.randint(0, top_number) #generate a random value from range zero upto and including top_number:

print("Okay let's go to guessing")
print()
print("Try to guess the value")
guesses = 0 #We want to count the number of guesses thus we are to considered the initial state before guessing the correct value

input()
while True: #while the below statements are true the loop has to iterate
    guesses += 1 
    user_guess= input()
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("Enter a valid number")
        continue
    if user_guess == random_number:
        print("You got it")
        break #stop the loop if guessed correct
    else:
        print("You got it wrong")#add the numbers of upto until the player gets it right

        

#now print out the number of attempted encountered
print("You got it right in " + str(guesses) + " guesses")
print()
