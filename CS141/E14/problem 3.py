def uun_letters(first_name, last_name):
    lastuser = last_name.lower()
    firstuser = first_name[0].lower()
    if len(lastuser) >= 6:
        print(lastuser[:6]+firstuser)
    else:
        print(lastuser+firstuser)