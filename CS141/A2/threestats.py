# Author: Grayson Koch
# Date: 1/31/23
# Program to find the mean and media of Three Values
import sys
#stores the 3 values as variables
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
#finds the media by comparing the three values
if (a >= b and b >= c) or (c >= b and b >= a):
    median = b
elif (b >= a and a >= c) or (c >= a and a >= b):
    median = a
elif (a >= c and c >= b) or (b >= c and c >= a):
    median = c
#finds the mean of the three numbers
mean = (a + b + c) / 3
print("Median: ",median)
print("Mean: ",mean)