# Author: Grayson Koch
# Date: 1/22/23
# Program to solve the difference between two times of day, assuming their in order of start, finish. 
# Usage:
# Program should be called as minutes.py (hour of first time), (minutes of first time), (am or pm), (hour of second time), (minutes of second time), (am or pm)
# such as: minutes.py  7 59 pm 8 01 pm
#          minutes.py 12 43 pm 2 34 am

import sys

#takes user inputs and creates variables from them for use in calculation
#converts hours to minutes
hour1 = int(sys.argv[1]) * 60
minutes1 = int(sys.argv[2])
amorpm1 = sys.argv[3] 
hour2 = int(sys.argv[4]) * 60 
minutes2 = int(sys.argv[5])
amorpm2 = sys.argv[6]

#adds minutes from hour amount and minutes amount
time1 = hour1 + minutes1
time2 = hour2 + minutes2

#checks if time is am or pm and adds time accordingly
if amorpm1 == "pm" and hour1 != 720:
    time1 = time1 + (12 * 60)
if amorpm2 == "pm" and hour2 != 720:
    time2 = time2 + (12 * 60)

#calculates time difference using if else statements
if hour2 < hour1 and amorpm2 == "am":
    finaltime = time2 - time1 + (24 * 60)
if time1 > time2:
    finaltime = time1 - time2
else:
    finaltime = time2 - time1
   
# finds the hour and minute difference to display properly
finalhour = finaltime // 60
finalminute = finaltime - finalhour * 60 

#prints the result
print("There are", finalhour, "hours and", finalminute,"minutes between the two times.")
    