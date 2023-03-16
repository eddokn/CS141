def remove_vowels(string):
    word = ""
    for i in string:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            word = word + i 
    print(word)