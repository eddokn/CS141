# Author:Grayson Koch
# Date:1/18/2023
# Description: Calculator to multiply float values without using a period

# get the first and second integers
firstInput = int(input("Please enter the first integer: "))
secondInput = int(input("Please enter a second integer: "))

# A. print out "Fixing notation!"
print("Fixing notation!")

# B. Extract the integer and decimal portions from the first integer input
firstInputInt = firstInput // 10
firstInputDec = firstInput % 10 * 0.1

# C. Print the reformatted first input
firstInputcomplete = firstInputInt + firstInputDec
print("The first value", firstInput, "reformatted is", firstInputcomplete)

# D. Extract the integer and decimal portions from the second integer input
secondInputInt = secondInput // 10
secondInputDec = secondInput % 10 * 0.1

# E. Print the reformatted second input
secondInputcomplete = secondInputInt + secondInputDec
print("The second value", secondInput, "reformatted is", secondInputcomplete)

# F. Perform calculations for the product of the reformatted (decimal) values
completeValue = firstInputcomplete * secondInputcomplete

# G. Print out the final result
print("The completed product is", completeValue)
