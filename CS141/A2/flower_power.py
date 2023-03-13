# Author: Grayson Koch
# Date: 1/31/2023
# Program for the perfumer encounter for the hit game FlowerPower!
# Debug testing to use program arguments instead of prompts
import sys
if len(sys.argv) > 1:
    stargazer = int(sys.argv[1])
    plumeria = int(sys.argv[2])
    star_trade = int(sys.argv[3])
    plum_trade = int(sys.argv[4])
else:
# Asks the user how many flowers they found and are willing to trade, with some narrative
    stargazer = int(input("How many Stargazer Lillies did you forage? "))
    plumeria = int(input("And how many Plumeria flowers? "))
    print("You continue your trek through the forest, hoping to find enough goods to finally get your hands on that shield the general store just put up for sale.")
    print("As you daydream of your shiny new protection, you trip over a trunk and land square in a bush.")
    print("Inside the bush, you find a perfumer! They immediately recognize the goods in your bag.")
    print('"I can give you a hefty sum for those pretties!" They say.')
    star_trade = int(input("How many Stargazer Lillies would you like to sell? "))
    plum_trade = int(input("And Plumeria Flowers? "))
#checks if the player is selling 0 flowers, or selling flowers they don't have
if star_trade > stargazer and plum_trade > plumeria:
    print("You can't sell me what you don't have!" )
elif star_trade == 0 and plum_trade == 0:
    print("Fall into my bush and sell me nothing? What a shame.")
else:
#Does the math on the emerald exchange based on flowers sold, and stores the emeralds as a variable
    if star_trade > 11 and star_trade % 12 != 0:
        print("The perfumer offers you", 5 * star_trade,"emeralds.")
        trade = 5 * star_trade
    elif (plum_trade >= 20 and star_trade % 12 == 0) and star_trade % 24 != 0:
        print("The perfumer offers you", plum_trade * 4,"emeralds.")
        trade = 4 * plum_trade 
    elif (plum_trade < 20 and star_trade % 12 == 0) and star_trade % 24 != 0:
        print("The perfumer offers you", plum_trade,"emeralds.")
        trade = plum_trade
    elif plum_trade >= 6 and star_trade < 11:
        print("The perfumer offers you", 3  * plum_trade,"emeralds.")
        trade = 3 * plum_trade
    elif plum_trade < 6 and star_trade < 11:
        print("The perfumer offers you", star_trade * 2, "emeralds.")
        trade = 2 * star_trade
#Asks the user if they accept the trade, and then lists their belongings
    agree = input("Do you accept the trade? (yes/no) ")
    if agree == "yes" or agree == "y" or agree == "Yes":
        print("You recieve", trade,"emeralds and retain",stargazer - star_trade,"Stargazer Lillies and",plumeria - plum_trade,"Plumeria Flowers.")
    else:
        print("You retain", stargazer,"Stargazer Lillies and",plumeria,"Plumeria Flowers.")
        
    