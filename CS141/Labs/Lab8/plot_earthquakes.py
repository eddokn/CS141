# Author: Grayson Koch
# Date: 3/2/23
# Description: Reads earthquake data from a csv file and plots it on a map

import turtle

# copied from my lab 5 solution:
def teleport(t, x, y):
    """ Move the turtle to (x, y), ensuring that nothing is drawn along the
        way. Postcondition: the turtle's orientation and up/down state is the
        same as before.
    """
    # save the current pen state
    pen_was_down = t.isdown()
    
    # pick up pen, move to coordinates
    t.up()
    t.goto(x, y)
    
    # restore pen state
    if pen_was_down:
        t.down()

# copied from A4, with a couple slight modifications:
def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle; return a turtle object in hidden
        state. The canvas has size canv_width by canv_height, with a
        coordinate system where (0,0) is in the center, and automatic
        re-drawing of the canvas is disabled. Set the background image to
        earth.png.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()
   
    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255
    
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement
    
    turtle.bgpic('earth.png') # set the background image
    turtle.update()
    return t

def parse_row(line):
    """ Parse a line of the csv file, returning a dict with keys
    for latitude, longitude, timestamp, and magnitude.
    Pre: line is an unprocessed string representing a line of the file.
    Post: the returned dict has the following keys with values according
          to the data in the given line of the file:
            "latitude" -> (float)
            "longitude" -> (float)
            "timestamp" -> (str)
            "magnitude" -> (float)
    """
    # split the line into its constituent numbers
    values = line.split(",")
    # create a dictionary and populate it with the given keys
    headers = ["latitude","longitude","timestamp","magnitude"]
    x = 0
    dictionary = {}
    for i in headers:
        if i != "timestamp":
            dictionary[i] = float(values[x])
        else:
            dictionary[i] = values[x]
        x += 1
    # return the resulting dictionary
    return dictionary
def main():
    """ Main function: plot a circle on a map for each earthquake """
    # we'll scale coordinates and canvas to be 720x360, double
    # the size of the range of lat/lon coordinates
    scale = 2.0
    
    # call turtle_setup to set up the canvas and get a turtle
    t = turtle_setup(scale * 360, scale * 180)
    
    # open earthquakes.csv for reading
    file = open("earthquakes.csv","r")
    next(file)
    # parse each line of the file using parse_row and add each returned
    dictionary_list = []
    for line in file:
        dictionary = parse_row(line)
    # dictionary into a list (skip the headers on the first line!)
        dictionary_list.append(dictionary)
    print(dictionary_list)
    # for each earthquake dictionary in the list:
    for dictionary in dictionary_list:
        # if the magnitude is larger than 1.0:
            if dictionary['magnitude'] > 1.0:
                # draw a circle with radius equal to the magnitude
                radius = dictionary['magnitude']
                # at (longitude * scale, latitude * scale).
                teleport(t, 2 * dictionary["longitude"], 2 * dictionary["latitude"])
                t.color
                t.circle(radius)

    # update the screen so all the circles are drawn on the canvas
    turtle.update()
if __name__ == "__main__":
    main()


