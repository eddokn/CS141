num = 1
loopnum = 1
while loopnum <= 6:
    num = num // 6 + 1
    print(num, end=" ")
    while num < loopnum * 6:
        num += loopnum
        if num < 10:
            print("",num,end=" ")
        else:
            print(num,end=" ")
    print("")
    loopnum += 1
    addition = loopnum