
a = list(range(10))

def lp() :
    b = list(a)
    return b

def tp() :
    b = tuple(a)
    return b

def main() :
    from timeit import timeit
    print("with list" , timeit(lp , number = 1))
    print("with tuple" , timeit(tp , number = 1))

    #? To return the sequence with least time of execution :
    x = timeit(lp , number = 1)
    y = timeit(tp , number = 1)
    print(f"list \ndifference - {y-x}" if x<y else f"tuple \ndifference - {x-y}")
    print('')

def lp1() :
    b = list(a)
    for i in b :
        return i

def tp1() :
    b = tuple(a)
    for i in b :
        return i

def mainloop() :
    from timeit import timeit
    x = timeit(lp1 , number = 100)
    y = timeit(tp1 , number = 100)
    print("loop with list --> " , x)
    print("loop with tuple --> " , y)
    print("::::::")
    print(f"list \ndifference - {y-x}" if x<y else f"tuple \ndifference - {x-y} seconds")

if __name__ == '__main__' :
    # main()
    mainloop()

#? From multiple results creation of tuples is faster than lists 
#? From multiple results loop through tuples is faster than lists 

#* In case of defining multiple values in a sequence which aren't supposed to be changed , tuple seems a better and faster option than lists in terms of iteration.

'''
1. Tuples are used where we don't need to change, add or remove any element. Using tuples also indicated developers that the value is not meant to change.
2. If you have to update, add or remove an element in a collection then lists should be used.
3. Tuples are faster than lists when iterating over the elements.
    So, if you are defining a constant set of values that you need to just iterate to then tuples should be the better choice for you.
4. You can't create a dictionary with lists as keys since dictionary doesn't accept mutable sequences as key
'''