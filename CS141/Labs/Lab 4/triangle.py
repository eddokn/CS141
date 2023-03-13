# Author: Grayson Koch
# Date: 2/1/23
# Program to draw an ascii pyramid with variable "heights"
import sys
#takes the width from program arguments
width = int(sys.argv[1])
#loop to construct the pyramid with given width
for w in range(1, width + 1):
    print("*" * w)
    if w == width:
        for w in range(width - 1 ,0,-1):
            print("*" * w)
    