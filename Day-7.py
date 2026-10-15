'''
Sequences ---> Strings,Lists,Tuples,Sets,Frozensets,Dicts

Strings --> A String is a group of characters,It is immutable,Ordered,Indexed
Collection.we can denote it in single,double or triple quotes...

data = ''#empty string
print(type(data))
print(len(data))

#Operations ---> Concatenation,Repetition,Indexed,Slicing
sub1 = "Python"
sub2 = "MYSQL"
print(sub1+sub2)
#output should be Python,MYSQL
#python <-> MYSQL
print(str("Python,MYSQL"))
print(f'{sub1},{sub2}')
print(sub1+" <-> "+sub2)

#Repetition --> String can be repeated any number of items with a valid int
print("*")
print('*'*10)
name = "Saketh";place = "Vizag"
print(f'{name * 10}*')
print(f'<--/|\-->{name} is in <--/|\-->{place}')

#Membership ---> in ,not in
print("jay" in "Ajay")
print("Jay" in "Ajay") #returns False

print("jay" not in "Ajay")

s = "codegnan"
print(len(s))
print(s[0])
print(s[21])#raises error index is out of range

#Indexing ---> Accessing each position(index) in an object
#It starts at 0 and ends at len(obj) - 1

name = "Codegnan"
print(name)
print(len(name))
#Traversing the elements ---> Positive Indexing
print(name[2])
print(name[7])
#print(name[21]) raises error as index is in out or range
#Negative Indexing ---> starts from back it is denoted as -1 to len(obj)
print(name[-1])
print(name[-4])
#print(name[-9]) #Index Error

#Slicing ---> group of characters ---> [start:end] start is included,end is
#excluded len(obj) - 1)

s = "Codegnan"
print(s[:])# returns all characters
print(s[0:])
print(s[0:4])
print(s[4:8])
print(s[4:21])#returns till end of string
print(s[0:21])
print(s[4:7])
print(s[24:])#returns empty
print(s[5:1])#returns empty string as positive slicing lower index to higher index

#name[2] = "saketh" #Strings are immutable

print(s)
print(s[-1:])# returns last character
print(s[-5:-1])# same including negative indices with same symbols lower to higher
print(s[:-6])
print(s[-6:])
print(s[-1:-5])#empty string
print(s[:-6]+s[-6:])
print(s[-1:-4]) #returns empty string


print(s)
print(s[1:-1])
print(s[-1:3])# returns empty

#Task ---> Create a string and explore above possibilities


#Striding ---> [start:end:step] ---> Now we can specifically get desired
#characters in an interval
s = "Codegnan"
print(s[::1])
print(s[::2])
print(s[::3])
#print(s[::0])#returns Value Error
print(s[::1])#returns complete string
print(s[::2])#skips each alternate element from begnning
print(s[::3])


place = "Visakhapatnam"
print(place[:4])
print(place[7:])
print(place[-6:])
print(place[1:7:2])#first perform [1:7] then skip one element in it
print(place[2:18:5])

#what if we give -1 in interval
print(place[::-1])#this helps to return in reverse order

print(place[::-2])# this skips one element in reverse order

#you can explore all cases in striding
print(place[1:9:-2])
print(place[-9:-1:1])
print(place[-7:-1:-3])
'''

#Built-in functions ---> type(),len(),min(),max(),ord(),chr(),sorted()

password = "admin123"
print(len(password))
print(type(password))
print(min(password)) # min() returns min objects in collection

#ASCII Values Follows
print(ord('A'))
print(ord('a'))
print(ord('z'))
print(ord('Z'))
print(chr(120))
print(sorted(password))



 


































 


































 

































 

































 






























