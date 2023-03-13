fin = open("fin.txt", 'r')
fot = open("fot.txt", 'w')

for line in fin:
    fl = line.strip().split(': ')

    fot.write(fl[-1])
    fot.write(fl[0])

fot.close()
fin.close()

fot = open("fot.txt", 'r')
a = fot.read(3)
fot.seek(8)
print(a, fot.read())
fot.close()