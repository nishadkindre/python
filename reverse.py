# reverse functions to return the reversed version of indexed type of collections.

#? Using for loop :- 
def reverse_string(x: str) -> str:
    '''Return a reversed copy of the entered string'''
    new = ""
    for i in range(len(x)-1,-1,-1):
        new += x[i]
    return new

def reverse_list(x: list) -> list:
    '''Return a reversed copy of the entered list'''
    new = []
    for i in range(len(x)-1,-1,-1):
        new.append(x[i])
    return new

def reverse_tuple(x: tuple) -> tuple:
    '''Return a reversed copy of the entered tuple'''
    new = []
    for i in range(len(x)-1,-1,-1):
        new.append(x[i])
    return tuple(new)

#? Using while loop :- 
def reverse_string_(x: str) -> str:
    new = ""
    i = -1
    while i>= -len(x):
        new += x[i]
        i -= 1
    return new

def reverse_list_(x: list) -> list:
    new = []
    i = -1
    while i>= -len(x):
        new.append(x[i])
        i -= 1
    return new
