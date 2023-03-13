# Author: Grayson Koch
# Date: 1/31/23
# Program to solve the quadratic formula given a, b, and c.
import sys
#takes values for a, b, and c from the program arguments
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
#checks for special cases that leave the formula undefined
if a == 0:
    print("These coefficients do not describe a quadratic.")
if (b ** 2 - (4 * a * c)) < 0:
    print("There are no real roots.")
else:
    #solves the quadratic formula with given values
    xplus = -b + ((b ** 2 - (4 * a * c)) ** 0.5)
    xplus = xplus / (2 * a)
    xminus = -b - ((b ** 2 - (4 * a * c)) ** 0.5)
    xminus = xminus / (2 * a)
    print(xplus,xminus)


