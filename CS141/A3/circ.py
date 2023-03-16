# Author: Grayson Koch
# Date: 2/4/23
# Program to print a circulant matrice from program arguments
import sys
#stores side length and top-left number for the square
sidelength = int(sys.argv[1])
firstnum = int(sys.argv[2])
#creates variables for the loop, and checking the length of the line
count = 0
length = 0 
#checks that the inputs are valid
if sidelength <= firstnum:
    print("The first number must be more than 0 and less than the side length")
else:
    #loop that creates the matrix with the given parameters 
    while count != sidelength - 1:  
        for x in range(0,sidelength):
    #checks to see that the number doesn't go over the given amount
            if firstnum == sidelength:
                firstnum = 0
            print(firstnum, end=" ")
            length += 1
    #uses variable length to determine how far the string goes, to add the space when needed
            if length == sidelength:
                print()
                print(firstnum, end=" ")
                length = 1
            firstnum += 1
        count += 1
    #prints the missing number from the loop 
    print(firstnum)
        
            
        