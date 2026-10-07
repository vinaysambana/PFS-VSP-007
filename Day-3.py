'''
# numeric data types -> integer  --> quantites,ordes,ids
age = 32
print(age)
print (type(age))
stock = 35
print (type(stock))
batch_rank = 1
print (batch_rank)


#float values --> salaries,price,percentage calculation,temperatures

salary = 31567.50
print(salary)
print(type(salary))

temp = 34.5
print(type(temp))

#complex --> real and imaginary values --> scientific calcns, signal processing

#i5 = 23
# data = 3+5i #in this case addition  will be done
#print(data)

data = 3+5j
print(data)
print(type(data))

#Boolean --> True/False --> Validations
access = True
print(type(access))
result = False
print(type(result))

#None Type --> None
#None --> 0,False,'',[],(),{},set() --> None cases in Python
Branch_rank = None
print(type(Branch_rank))

#Type Conversions -> Converting one data type to another data type
# explicit conversion

#integer --> float,complex,boolean
#Every built-in data type is a built-in function
rank = 5
print(type(rank))
b = float(rank)
print(b)
print(type(b))
c= complex(rank)
print(c)



# bool (anything) is True
# bool (nothing) is False
d=bool(rank)
print(d)
print(type(d))

bool(0)
bool(None)
bool('')
bool([])
bool([''])
bool([0])

#space is also a character
print(bool([ ' '])) # empty string inside a list

#float --> integer,complex,boolean

temperature = 27.9
print(temperature)

T=bool(temperature)
print(type(T))
print(T)
T=int(temperature)
print(T)
T=complex(temperature)
print(T)

#complex --> int,float, boolean
signal = 5+6j
#c = int(signal) # raises TypeError (in valid datatype)
#print(c)
#d= float(signal)
e = bool(signal)
print(e)

access = True
int(access)
print(int(access))

access = True
float(access)
print(float(access))


access = True
complex(access)
print(complex(access))

access = True
bool(access)
print(bool(access))


a = int(float(bool(5)))
print(a)

b = bool(float(int(35))) # check for the outer one
print(b)

c = True+35+3.5+(6+5j) #True becomes 1
print(c)

#sequence types --> strings,lists,sets,frozen sets,dictionaries
#strings--> Group of characters
#quotations -->single,double,triple quotes

place = "codegnan"
print(type(place))
name = 'vinay'
print(name)
#strings are Immutable,Ordered,Indexed Collection
print(len(name)) #len(obj) --> returns the number of items in a collection
print(len(place))
print(len('qwerty'))
# space is also a character
a = ""
print(a)
print(len(a))
'''
#converting strng --> int,float,complex,boolean
course = 'Python'
#print(int(course)) #value Error
#print(float(course)) # raises value Error
#print(complex(course))
print(bool(course))

#int -->str
#float  -->str
#complex-->str
#bool -->str

data = 56
b = str(data) # it becomes numeric string
print(b)

mileage = 13.5
c = str(mileage)
print(type(c))
d = str(3+5j)
print(d)
e = str(True)
print(e)



































































