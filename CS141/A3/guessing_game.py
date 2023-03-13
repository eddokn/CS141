# Author: Grayson Koch
# Date: 2/10/23
# Guessing game for two letters in the word bellinghame for the hit studio NostalgiaSoft
import sys
import random
#variables for user's attempt amount and player or debug mode
attempts = int(sys.argv[1])
mode = sys.argv[2]
firstcorrect = False
secondcorrect = False
i = 0
# explains the game to the user
print("""===================================================================================================================
Hello and welcome to a better time for games! Prepare for a nostalgia trip back to your Apple 2 text-scrollers.
The goal of the game is to correctly guess 2 letters from the word "Bellingham" with your given amount of attempts.
Good luck!
===================================================================================================================""")
#Checks to see which mode the game is in, and assigns the letters to be guessed based on this result 
if mode == "DEBUG":
    firstletter = sys.argv[3]
    secondletter = sys.argv[4]
else:
    firstletter = random.choice("bellingham")
    secondletter = random.choice("bellingham")
#Loop to have the user guess the letters, checking for the amount of attempts and if they get letters correct
while i < attempts and (firstcorrect == False or secondcorrect == False):
    i += 1
    print("""-------------------
Attempt""",i)
    guess = input("Guess a letter: ")
    if guess == firstletter or firstcorrect == True:
        firstcorrect = True
        print("You got the first letter!")
    else:
        print("That's not the first letter")
    if guess == secondletter or secondcorrect == True:
        secondcorrect = True
        print("You got the second letter!")
    else:
        print("That's not the second letter!")
#Checks to see if the user won or ran out of guesses 
if firstcorrect == True and secondcorrect == True:
    print("You guessed the secret letters",firstletter,"and",secondletter+". Congratulations!")
else:
    print("Good try! The secret letters were",firstletter,"and",secondletter+".")