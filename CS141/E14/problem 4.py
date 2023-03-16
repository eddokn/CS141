def capitalize_words(string):
    count = 0
    firstletter = string[0].replace(string[0],string[0].upper())
    string = string[1:]
    for z in string:
        count += 1
        if z == " ":
            string = string.replace(" "+string[count]," "+string[count].upper())
    print(firstletter+string)
    
    
    