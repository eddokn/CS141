words = ["something","else"]
text = ["something","not"]

def censor(text,words):
    for i in words:
        if i in text:
            text.remove(i)
    return text

def wordduplicates():
    answer = ""
    words = []
    while answer != "exit":
        answer = input("input a word: ").lower()
        if answer not in words and answer != "exit":
            words.append(answer)
            print("That's not a duplicate!")
        elif answer in words:
            print("That's a duplicate!")

def is_sorted(my_list):
    userlist = my_list
    print(userlist,my_list)
    my_list.sort()
    print(userlist,my_list)
    if userlist == my_list:
        print("List is sorted!")
    elif userlist != my_list:
        print("List isn't sorted!")
    