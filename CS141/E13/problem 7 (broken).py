def print_banner(string):
    i = 0
    c = len(string)
    if c <= 80:
        while i <= c + 1:
            print("#",end="")
            i += 1
    else:
        while i <= 80:
            print("#",end="")
            i += 1
    i = 0 
    print()
    print("#",end="")
    if c <= 80:
        print(string, end="")
        print("#")
    elif c > 80:
        while c > 0:
            for y in range(0,80):
                print(string[y],end="")
                l = y
            print("#")
            print("#",end="")
            c -= l 
    while i <= len(string) + 1:
        print("#",end="")
        i += 1
    
