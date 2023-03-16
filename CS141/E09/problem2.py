import random
import sys
d = int(sys.argv[1])
n = int(sys.argv[2])
for x in range(n):
    print(random.randint(1,d),end=" ")
    