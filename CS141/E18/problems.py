def copy_list(inlist):
    """ Return a new list object containing
        the same elements as in_list.
        Precondition: in_list's contents are
        all immutable. """
    copylist = inlist[:]
    return copylist
    
import random
def snap(avengers):
    """ Remove a randomly chosen half of the
    elements from the given list of avengers
    """
    halfpoint = len(avengers) // 2
    if random.randint(0,1) == 1:
        avengers = avengers[:halfpoint]
    else:
        avengers = avengers[halfpoint:]
    return avengers

    