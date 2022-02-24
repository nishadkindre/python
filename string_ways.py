
#? format() function offers convenience and better readability
#? Cases where requirements of printing numerous variable would clutter the syntax when using regular or fstring method

#* format function enables the viewer to get a precise view of the variables used 
#* wherein, variables bundled in a tuple could be used multiple times in a string given access of their index number

#* format func includes the variables defined under it at spacified positions in a string 
#* places the variable values in {} in a string 

# TODO : STUDY MULIPLE EXECUTIONS OF THE CODE AND CONCLUDING THE FASTEST WAY OF REPRESENTING DATA IN A STRING

names = ['nishad' , 'pranav' , 'chinmay' , 'vedant']
courses = ['c' , 'css' , 'cpp' , 'python']

#? FORMAT FUNCTION
def op() :
    for i in range(0 , len(names)) :
        a = "Name : {}\tCourse : {}"
        #* a = "Name : {1}\tCourse : {0}" --> places variables with their respective index number when defined under the format() --> {1} will return variable at index no. 1 in its place
    return(a.format(names[i],courses[i]))

#? REGULAR METHOD
def op1() :
    for i in range(0 , len(names)) :
        return("Name :", names[i], '\t'"Course : ", courses[i])

#? F STRING METHOD
def op2() :
    for i in range(0 , len(names)) :
        return(f"Names : {names[i]}\tCourses : {courses[i]}")

#? % STRING METHOD
def op3() :
    for i in range(0 , len(names)) :
        return("Names : %s\tCourses : %s" %(names[i] , courses[i]))

#? PLUS METHOD
def op4() :
    for i in range(0 , len(names)) :
        return("Name :" + names[i] + '\t'"Course : " + courses[i])

#* We use timeit module to return the execution time 
def main() :
    from timeit import timeit
    print('using format function :\t\t' , timeit(op , number = 1))
    # print('regular method :\t\t' , timeit(op1 , number = 1))
    # print('f string method :\t\t' , timeit(op2 , number = 1))
    print('%\ string method :\t\t' , timeit(op3 , number = 1))
    # print('plus method :\t\t\t' , timeit(op4 , number = 1))

if __name__ == '__main__' :
    main()
