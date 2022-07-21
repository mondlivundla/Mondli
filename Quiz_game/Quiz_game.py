"""
We should welcome anyone who opens the game, but first ask their preferred username
"""
print("Hello there, what is your preferred username: ")
username = input()
print("Welcome " + str(username) + " to Mondli's General quiz game! ")

#Ask the user if he/she wishes to play the quiz game
answer = input("Do you wish to play the game?")
if answer.lower() == "yes" or "y":
    print("Well let's play mate") #A 'yes' or 'no' response should be considered no matter which type of alphabetic format, whether small or big caps
    score = 0
else:
    quit() 
""""close the game on the spot when the user decides not to play the quiz game

if the player agrees to playing the quiz game then jump to questions without doubt
"""
#Question 1
answer = input("What does DB stand for in computer languange? ")
if answer.lower() == "database":
    print("That's very correct mate!")
    score += 1 #add 1 mark for a correct answer
else:
    print("Answer incorrect! ") #Give the player a chance to re-take the question one last time

    print()
    answer = input("What does DB stand for in computer languange? ")
    if answer.lower() == "database":
        print("Correct answer")
        score += 0.5 #Player gets half a mark for getting the answer correct on the second trial
    else:
        print("Am sorry my friend that's wrong! ")

#Question 2
answer = input("What does CV stand for? ")
if answer.lower().strip() == "carriculum vitae": #the (.lower()) function should allow the user to input any kind of letters, whether small or upper case, or the combination of the two
    print("That's very correct mate!")
    score += 1 #add another mark for a correct answer on top of the already earned mark

else:
    print("Last chance! ") #Give the player 2 chances to give the correct response

    print()
    answer = input("What does CV stand for? ")
    if answer.lower().strip() == "carriculum vitae":
        print("That's very correct mate!")
        score += 0.5 #add half a mark for the second try

    else:
        print("Ooops sorry mate you got it wrong Again")

#Question 3
answer = input("What does RAM stand on a computer? ")
if answer.lower() == "random access memory":
    print("That's very correct my friend!")
    score += 1 #add another mark for a correct answer on top of the already earned mark

else:
    print("Last chance! ") #Give the player 2 chances to give the correct response

    print()
    answer = input("What does RAM stand on a computer? ")
    if answer.lower() == "random access memory":
        print("That's very correct mate!")
        score += 0.5 #add half a mark for the second try

    else:
        print("Ooops sorry mate, wrong answer!")

#Question 4
answer = input("What does CPU stand for in computers? ")
if answer.lower() == "central processing unit":
    print("Yes you're correct")
    score += 1
else:
    print("Wrong answer, last chance better make sure you get it right this time")#Give the player another chance to answer the question

    print()
    answer = input("What does CPU stand for in computers? ")
    if answer.lower() == "central processing unit": #the answer is considered true irregardless of case type, lower or upper case is not is of interest as long as we included the (.lower()) function
        print("Now you finally got the answer right! ")
        score += 0.5
    else:
        print("Your answer is still wrong sorry and your chance has been wasted, now you can view your final score")

print()
print("Your final score is " + str(score))
print("Your percentage is " + str((score / 4) * 100) + "%.")
print()
