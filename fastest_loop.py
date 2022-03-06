
# TODO : SUM THE NUMBERS FROM  0 TO N
# CONDUCTING DIFFERENT METHODS FOR THE EXECUTION OF THE ABOVE TASK AND ANALYSING THEIR EXECUTION DURATION DIFFERENCE

#? WHILE LOOP 
def while_loop(n=100_100_100): # underscores can be used in integer literals
    sum = 0
    num = 0
    while num <= n :
        sum += num
        num += 1
    return sum

#?  FOR LOOP
def for_loop(n = 100_100_100):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

#?  FOR LOOP WITH INCREMENT
def for_loop_with_increment(n = 100_100_100):
    sum = 0
    for num in range(n + 1):
        sum += num
        num += 1
    return sum

#? TESTING FOR A CONDITION 
def for_loop_with_test(n = 100_100_100):
    sum = 0
    for num in range(n + 1):
        if num < n : pass
        sum += num
    return sum

#?  FOR LOOP WITH INCREMENT AND TEST
def for_loop_with_increment_and_test(n = 100_100_100):
    sum = 0
    for num in range(n + 1):
        if num < n : pass
        sum += 1
        num += 1
    return sum

#? WITH BUILTIN SUM AND RANGE FUNCTION 
def sum_range(n=100_100_100):
    return sum(range(n))

#? NUMPY  
import numpy
def sum_numpy(n=100_100_100) :
    return numpy.sum(numpy.arange(n))

#? PURE MATH 
def sum_math(n=100_100_100):
    return (n * (n - 1)) // 2

import timeit
def main() :
    print('while loop\t\t' , timeit.timeit(while_loop , number = 1))
    print('for pure\t\t' , timeit.timeit(for_loop , number = 1))
    print('for increment\t\t' , timeit.timeit(for_loop_with_increment , number = 1))
    print('for test\t\t' , timeit.timeit(for_loop_with_test , number = 1))
    print('for inc+test\t\t' , timeit.timeit(for_loop_with_increment_and_test , number = 1))
    print('sum range\t\t' , timeit.timeit(sum_range , number = 1))
    print('sum numpy\t\t' , timeit.timeit(sum_numpy , number = 1))
    print('sum math\t\t' , timeit.timeit(sum_math , number = 1))

if __name__ == '__main__' :
    main()

#? Python is written in C 

#! Python is a slow language and doing useless operations slows our code

#*  use built ins over loops wherever you can

#*  in numpy both the addition and iteration is done in C 
#*  creation of arange actually creates that whole array in memory , we made a 100M element array in memory

#*  sum range wont create all those elements in the memory,so it can run any desirable number without having any constraints over memory consumption

#*  sum math is a pure python and it beats out the C one by a lot

#!     NOTE : FASTEST WAY TO LOOP IN PYTHON IS NOT TO LOOP IN PYTHON
#!     REMEMBER : if you have the liberty of computing the answer mathematically ahead of time,its the best option

#* Precedence :
    #* mathematically
    #* in  a pure C function
    #* call a pure C function
    #* use python builtins like sum or map rather than wrtiting the loop yourself
    #* the last resort should be using a for loop over a while loop
