def find(v,lst):
    count = 0 
    for i in lst:
        if i == v:
            return count
        count += 1
    return -1

def remove_all(v, lst):
    for i in lst:
        if i == v:
            lst.remove(v)
    return lst
    
    
def without(v, lst):
    newlist = []
    for i in lst:
        if i != v:
            newlist = newlist + [i]
    return newlist
            
def findlessthanindex(v, sorted_lst):
    null
    
 