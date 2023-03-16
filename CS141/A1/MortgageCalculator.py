# Author: Grayson Koch
# Date: 1/21/23
# Program that prompts the user for mortgage information
# and outputs the montly payment

import sys

# Checks for command line arguments and uses them in the
# calculation without prompting for inputs
if len(sys.argv) > 1:
    P = sys.argv[1]
    D = sys.argv[2]
    N = sys.argv[3]
    R = sys.argv[4]
    P = float(P)
    D = float(D)
    N = float(N)
    R = float(R) * 0.01 / 12
else:
    #Prompts the user for the price of the home, down payment,
    # number of months, and montly interest rate to be used
    # in the calculation
    # This happens if command-line arguments are not provided
    P = float(input("Price of the home (P):"))
    D = float(input("Down Payment (D):"))
    N = float(input("Number of months (N):"))
    R = float(input("Interest rate by year (R):")) * 0.01 / 12

# Uses information given by user to calculate the monthly payment
# and then prints the value 
M1 = P - D
M2 = R * ((1 + R) ** N)
M3 = ((1 + R) ** N) - 1
M = M1 * (M2 / M3)
print(M)
        
