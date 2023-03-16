# Author: Grayson Koch
# Date: 1/24/23
# Program to check user's age and citizenship and tells them if they're elgible
# to be a senator or representitive

#Asks for the person's age and citizenship
age = int(input("How old is the person? "))
citizenshipage = int(input("How many years have they been a citizen? "))

#CHecks if the person's data fits either requirements and states which applies
if age >= 30 and citizenshipage >= 9:
    print("They can run for Senator and Representative")
elif age >= 25 and citizenshipage >= 7:
    print("They can run for Representitive")
else:
    print("They can run for neither office")