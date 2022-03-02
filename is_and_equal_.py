
'''
        == --> value equality --> Two objects have the same value
        is --> reference equality --> Two references refer to the same object , have the same memory location

'''

#*! ==  returns True in case of value equality 
#*! is  returns True in case of reference equality 

#*? Using inbuilt function id() to return the unique id / memory address of the input 
a = [1,2,3]
print(id(a))

b = [1,2,3]
print(id(b))

c = a
print(id(c))

d = a.copy() #? returns only a copy with no reference of d to a
print(id(d))

e = []
e.extend(a)
print(e)

print(b == a)    #*? --> true as there is value equality between a and b
print(b is a)    #*? --> false as both a and b are pointing different list,

print(c == a)    #*? --> true as c has the value of a
print(c is a)    #*? --> true as c and a pointing towards a same list

print(c == b)    #*? --> true as c having the value of a is similar to b
print(c is b)    #*? --> false as both c and b have different reference

print(d == a)    #*? --> true as d being a copy of a will contain same values
print(d is a)    #*? --> false as d and a have different references
print(d == c)    #*? --> true due to value equality 
print(d == b)    #*? --> true due to value equality 

print(e == a)    #*? --> true as there is value equality between a and e
print(e is a)    #*? --> false as both a and e are pointing different list

c[1] = 0         #*? --> changes the value of a as well due to reference equality in both
d[1] = 9         #*? --> change done in d only
print(a,b,c,d,e) #*? --> no change in b , e
