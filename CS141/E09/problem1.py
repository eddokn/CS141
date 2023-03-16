import random
x = random.randint(1,11)
intcount = 0
while x <= 8:
    print(x)
    x = random.randint(1,11)
    intcount += 1
print("Generated",intcount,"numbers")

