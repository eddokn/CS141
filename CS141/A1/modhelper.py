# Author: Grayon Koch
# Date: 1/22/23
# Program that quizzes the user on the answer of the % operand
# with two numbers of their choosing

#import sys and create variable for final score
import sys
score = 0 

#Checks if user supplied command line arguments and creates variables
#for their numbers and answers
if len(sys.argv) > 1:
    firstnumber = int(sys.argv[1])
    secondnumber = int(sys.argv[2])
    firstanswer = int(sys.argv[3])
    secondanswer = int(sys.argv[4])
else:
    #Prompts the user for their numbers and answers
    firstnumber = (input("First Number:"))
    secondnumber = (input("Second Number:"))
    firstanswer = int(input("What is "+firstnumber+" % "+secondnumber+"? "))
    secondanswer = int(input("What is "+secondnumber+" % "+firstnumber+"? "))
    
#Solves for the user's two numbers 
firstnumber = int(firstnumber)
secondnumber = int(secondnumber)
firstmodsecond = firstnumber % secondnumber
secondmodfirst = secondnumber % firstnumber
firstdivsecond = firstnumber // secondnumber
seconddivfirst = secondnumber // firstnumber

#Checks user's answers for correctness and prints the results
if firstanswer == firstmodsecond:
    score = score + 1
    print("Correct!")
    print(firstnumber, "mod", secondnumber, "is", firstdivsecond,"remainder", firstmodsecond)
else:
    print("Incorrect!")
    print(firstnumber, "mod", secondnumber, "is", firstdivsecond,"remainder", firstmodsecond,"not",firstanswer)
print("")
if secondanswer == secondmodfirst:
    score = score + 1 
    print("Correct!")
    print(secondnumber, "mod", firstnumber, "is", seconddivfirst,"remainder", secondmodfirst)
else:
    print("Incorrect!")
    print(secondnumber, "mod", firstnumber, "is", seconddivfirst,"remainder", secondmodfirst,"not",secondanswer)

#Prints the user's final score
print("")
print("Your total is", score,"out of 2")



                