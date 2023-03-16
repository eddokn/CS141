def remove_comments(string):
    code = ""
    for i in string:
        if i != "#":
            code += i
        if i == "#":
            return code
    return code
       