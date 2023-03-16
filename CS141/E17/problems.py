def charcount(in_string):
    uniquecharacters = {}
    for i in in_string:
        if i not in uniquecharacters:
            uniquecharacters[i] = in_string.count(i)
    return uniquecharacters

def strmode(in_str):
    maxchar = max(charcount(in_str), key=charcount(in_str).get)
    return maxchar 
    
def dict_intersection(d1,d2):
    d3 = {}
    for key in d1:
        if key in d2:
            d3[key] = d1.get(key) + d2.get(key)
    print(d3)
    
def same_elements(list1, list2):
    print(list1,list2)
    if sorted(list1) == sorted(list2):
        print("True")
    else:
        print("False")

            