def remove_vowels(string):
    string = string.replace("e","").replace("a","").replace("i","").replace("o","").replace("u","")
    return string

def remove_comments(string):
    word = string.find("#")
    print(string[0:word])

def uun_letters(first_name, last_name):
    lastuser = last_name.lower()
    firstuser = first_name[0].lower()
    if len(lastuser) >= 6:
        print(lastuser[:6]+firstuser)
    else:
        print(lastuser+firstuser)
        
def capitalize_words(string):
    count = 0
    firstletter = string[0].replace(string[0],string[0].upper())
    string = string[1:]
    for z in string:
        count += 1
        if z == " ":
            string = string.replace(" "+string[count]," "+string[count].upper())
    print(firstletter+string)