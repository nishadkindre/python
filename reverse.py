# reverse function to return the reversed version of indexed type of collections.

def reverse_string(x: str) -> None:
    '''Return a reversed copy of the entered string'''
    for i in range(len(x)-1,-1,-1):
        print(x[i], end="")

def reverse_list(x: list) -> None:
    new = []
    for i in range(len(x)-1,-1,-1):
        new.append(x[i])
    print(new)

def reverse_tuple(x: tuple) -> None:
    new = []
    for i in range(len(x)-1,-1,-1):
        new.append(x[i])
    print(tuple(new))