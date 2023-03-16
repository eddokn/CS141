# Author: Grayson Koch
# Date: 2/15/23
# Program to calculate the total square footage of a home
def main():
    """ Prompts the user for the number of rooms to use in calculation
        This compiles all the areas calculated and returns the total value"""
    totalfootage = 0 
    rooms = int(input("What is the number of rooms? "))
    for i in range(1,rooms + 1):
        totalfootage += room_square_feet(str(i))
    print("Total square footage:",totalfootage)  
def room_square_feet(i):
    """ Takes the user's input to designate if the room is square
        or rectanglular
        This calls the prompt_user function and returns the area of the room"""
    roomtype = input("What is the shape of room "+i+"? ")
    squarefoot = prompt_user(roomtype)
    return squarefoot
def prompt_user(roomtype):
    """ function to ask the dimensions of the room
        This returns the area
        This uses the value given in room_square_feet"""
    if roomtype == "square":
        area = float(input("What is the side-length of the room? ")) ** 2
    elif roomtype == "rectangle":
        length = float(input("What is the length of the room? "))
        width = float(input("What is the width of the room? "))
        area = length * width
    return area
if __name__ == "__main__":
    main()
    

     