# Author: Grayson Koch
# Date: 2/10/23
# Midterm Exam, CSCI 141, Winter 2023

#During the current season, the following crops are available to the player:

#          Crop     Weeks    Seed Price    Sale Price
#        garlic         5         $0.08         $1.20
#        tulips         8         $0.18         $2.30

#  Weekly grocery budget: $9.0
import sys
#Takes variables for week in the season, bank account balance, garlic seeds planted, and tulip seeds planted.
weeks = int(sys.argv[1])
balance = float(sys.argv[2])
garlicamount = int(sys.argv[3])
tulipamount = int(sys.argv[4])
garlicseeds = 0
tulipseeds = 0 
#creates variables for the garlic and tulips' harvest times
garlicharvest = 5
tulipharvest = 8
count = 0
#variables for automatically buying seeds
autogarlic = 0
autotulip = 0
#states the length of the season and bank balance
print("The season will be", weeks,"weeks long, and your starting balance is $",balance)
#Loop that plays the game! Uses the variable count to track weeks and checks the player's
#balance and seed amounts, as well as time to harvest
#Not enough time to get the auto functionality :( 
while count != weeks and balance >= 0:
    garlicharvest = garlicharvest - 1
    tulipharvest = tulipharvest - 1
    balance = balance - 9
    if garlicharvest == 0:
        garlicearnings = 1.20 * garlicseeds
        balance = balance + garlicearnings
        garlicseeds = 0 
        print("You sell your harvest of garlic and earn $",garlicearnings)
    if tulipharvest == 0:
        tulipearnings = 2.30 * tulipseeds
        balance = balance + tulipearnings
        tulipseeds = 0
        print("You sell your harvest of tulips and earn $",tulipearnings)     
    if garlicseeds == 0:
        print("You're out of garlic!")
        balance = balance - (garlicamount * 0.08)
        print("You spent $",garlicamount * 0.08)
        garlicseeds = garlicamount
        garlicharvest = 5
    if tulipseeds == 0:
        print("You're out of tulips!")
        balance = balance - (tulipamount * 0.18)
        print("You spent $",tulipamount * 0.18)
        tulipseeds = tulipamount
        tulipharvest = 8
    print("""--------
Week""", count)
    print("Your current balance is $",balance)
    count += 1
if balance <= 0:
    print("You ran out of money! Try again!")
else:
    print("You enjoyed a successful season and ended with $",balance)
