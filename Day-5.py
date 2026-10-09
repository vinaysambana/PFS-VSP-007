'''
Operators --> Operators help us to perform operations between operands

Arithemetic Operators --> +,-,*,/,**,//(Integer or Floor Division),
%(Modulus---> Remainder)

Assigniment Operators --> It Helps us assign,update(increment),
decrement values

# = (assigning),
#+=(Addition& Assign),
#-=(subtraction& Assign)
#/=,//=,**=,%=

data = 20
print(data)
print(type(data))

stock = data
print(stock)

#Increment the value of stock
stock = stock + 5 # stock+=5
print(stock)
print(data)

#decrement the value of data by 2 values
data=data-2
print(data)
stock-=data #stock = stock - data
print(stock)

data *=5
print(data)

data/=4
print(data)

stock = 100
stock**=2
print(stock)

# Comparision Operators (Relational Operators)--> it performs comparision
# between the operands and results in boolean True/False --> Conditions
# ==,!=,<,<=,.,>=

name = 'Vinay'
vinay_attendance = 75
print(vinay_attendance >=80)
print(vinay_attendance ==80)
print(vinay_attendance <=80)
print(vinay_attendance <80)
print(vinay_attendance >80)
print(vinay_attendance !=80)

#Logical Operators--> and,or,not
#and --> it needs all conditions to be satisfied(two or more)
#or ---> it needs any one contition to be satisfied
#not --> oop to existing

max_marks = 80
vinay_marks = 75
max_att = 70
vinay_att = 70

certificate = vinay_marks >= max_marks and vinay_att >= max_att
print(certificate)

vinay_marks =+10
certificate = vinay_marks >= max_marks or vinay_att >= max_att
print(certificate)
chance = vinay_marks >= max_marks or vinay_att >= max_att
print(chance)


data = []
print(data)
print(not(data)) #returns True
data = [1,2,3,4] 
print(not(data)) #returns False as data is existing

#Both Logigal and comparision operators will return result
#in boolean

#Membership Operators --> in,not,in

names = ['vinay','vijay','balakrishna','raju']

name = 'ajay'
print(name in names)# returns False
print(name not in names)# returns True
print('12' in '121')
print('21' in '121')

#print(12 in 121) #Type Error as we have taken int type

print('ajay' in 'ajay kumar')#returns True as we are checking type as string
print(['ajay'] in ['ajay']) #returns False as its a list

#Identity Operators --> It specifically refres to the Object
#(memory location)
#id --> is,is not

a = 15
b = 15
print(a==b)
print(id(a))
print(id(b))

c = a
print(id(c))

print(c is a)# as id of both a and c are same it returns True

a = [1,2,3,4]
b = [1,2,3,4]
print(a==b)
print(id(a))
print(id(b))
# as we have taken two lists eventhough with similar values identity
print(a is b)

c = a
print(id(c))
print( c is a)# returns True as we are assigning same object

a = (1,2,3)
b = (1,2,3)
print(id(a),id(b))
print(a is b)

# when we checks with the Interpreter mode and scripting mode above
#tuple results changes

#Logical,Membership,Identity,Comparision (relational) --> always result is in Boolean
'''

#Bitwise Operators --> It performs Bitwise operations -->
#&(Bitwise and),| (Bitwise or),^(Bitwise xor)
#an integer will be converted binary format and performs bitwise operation
#following integer to binary conversion

print(7&3)
print(7|3)
print(7^3)# XOR operation it returns 4
#7 to binary ---> 0111
#3 to binary ---> 0011
#7^3 --> 0100

#shifting operators(<<,>>)
print(7<<1)
print(7>>1)




















