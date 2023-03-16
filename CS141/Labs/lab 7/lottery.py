# Author: Grayson Koch
# Date: 2/21/23
# Description: Program for the new and innovative lotto! Makes a user guess with a word and letter from a list

import sys
import random

def random_pick(words, numbers):
    """ Generate a random winning lottery pick. The winning
    pick is a string containing one item from words (a list
    of strings) and one item from numbers (a list of ints),
    concatenated in a randomly chosen order. The random
    choices are made independently, so the chance of each
    possible pick is equal."""
    
    # (TASK 1) - Pseudocode:
    # Pick one of the numbers randomly
    number = random.choice(numbers)
    # Pick one of the words randomly
    word = random.choice(words)
    # Pick which order they go in randomly
    order = random.randint(0,1)
    if order == 1:
        winner = number+word
    else:
        winner = word+number
    # return the combined lottery pick as a string
    return winner
 

def get_guess(words, numbers):
    """ Prompt the user until they enter a pick that contains one
        of the given words and begins or ends with one
        of the given numbers. When a valid guess is entered, return
        it.
        Precondition: numbers contains only one-digit numbers. """
    valid = False
    word = False
    number = False
    # (TASK 2) - Pseudocode:
    # while the user has not entered a valid pick:
    while valid != True:
    #    prompt the user for a pick
        answer = input("Enter your pick: ")
    #    check if it's valid (see docstring for the precise definition of valid)
        for i in words:
            if i in answer:
                word = True
        for i in numbers:
            if i in answer:
                number = True
    #    if not, print a message saying what's missing
        if word == False or number == False:
            if word == False:
                print("You need to use a word from the list!")
            if number == False:
              print("You need to use a number from the list!")
            word = False
            number = False
    #    if it is, return the valid pick
        if word == True and number == True:
            return answer

def main():
    """ Generate a lottery pick and check whether a user has guessed it
        correctly.  """
    word_choices = ["shucksan", "baker", "glacier"]
    number_choices = ["1", "2", "3"]
    
    print("Welcome, and thanks for playing Lotter.io!")
    print("Today's word choices are:", end=" ")
    print(word_choices)
    print("and the number choices are", end=" ")
    print(number_choices)
    print("The winning pick is a word and a number, in either order.")

    # (TASK 0) - Pseudocode:
    # if the program was run with no command line arguments:
    #     generate a winning pick by calling the random_pick function
    if len(sys.argv) <= 1:
        winner = random_pick(word_choices,number_choices)
    # otherwise:
    #     use the first command-line argument as the winning pick
    elif len(sys.argv) > 2:
        winner = sys.argv[1]
    
    # Get a guess from the user:
    guess = get_guess(word_choices,number_choices)
    
    #check if the guess is valid. If it is not, ask again.
    
    # (TASK 3) - Pseudocode:
    # determine the user's word and number choices by checking
    # whether the first or last character is among number_choices,
    # then split the string into the number part and the word part
    if guess[0] in number_choices:
        usernumber = guess[0]
        userword = guess[1:]
    else:
        letters = int(len(guess))
        usernumber = guess[letters-1]
        userword = guess[:letters-2]
    # print a message for whichever of the following cases is applicable:
    #   - their pick matches character for character, therefore they win
    if guess == winner:
        print("Congratulations! You win!")
    #   - the word and number are both correct but the pick doesn't match
    elif usernumber in winner and userword in winner:
        print("You guessed the correct number and word, but in the wrong order or with extra characters")
    #   - the word is correct but the number is incorrect
    elif userword in winner and usernumber not in winner:
        print("You guessed the correct word but not the correct number.")
    #   - the number is correct but the word is incorrect
    elif usernumber in winner and userword not in winner:
        print("You guessed the correct number but not the correct word.")
    #   - all other cases: neither the word nor the number is correct
    else:
        print("You guessed neither the correct word nor the correct number.")
        
if __name__ == "__main__":
    main()
