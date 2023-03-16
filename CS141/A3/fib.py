# Author: Grayson Koch
# Date: 2/4/23
# Program to cumpute the fibonacci number and golden ratio for a given integer
import sys
#assigns the integer to value n, and creates variables for calculation
n = int(sys.argv[1]) 
n1 = 0
n2 = 1
nton = 0

if n == 0:
    print("Fibonacci: 0 Golden: 0")
elif n == 1:
    print("Fibonacci: 1 Golden: Infinity")
else:
#adds numbers together up to the nth integer
    for i in range(0,n):
        #adds the last two numbers' results that are stored after each run 
        nton = n1 + n2
        #used to save fn - 1 for the golden ratio
        golden = n1
        n1 = n2
        n2 = nton
    #finds the golden ratio from the provided number
    golden = n1 / golden
    #prints results from both calculations
    print("Fibonacci:",n1,"Golden:", golden)