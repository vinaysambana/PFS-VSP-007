'''
#Lists -->A list is an Ordered,Mutable,Indexed and Heterogenous collection
#we use [] to represent lists
#students details,order details, stock entries.....
details = [1,'vinay','PFS7','vizag',56.7]
print(len(details))
print(type(details))

stu_ids = ['CGVI0134','CGVI0135','CGVI0136']
print(stu_ids[1])
#print(stu_ids[1])
stu_ids [0] = 'codegnan' #here we are using indexing
print(stu_ids)


#Tuples --> Tuples are also Immutable,ordered,Indexed and Heterogenous
#collections, we use () parenthesis

places = ('hyderbad','vizag','vjwda')
print(places)
#print(len(places))
#print(type(places))
places[0] = 'chennai'# it is not possible as Tuple are Immutable hence it throws an Error
print(places)

dimensions = 10,20,30# by default it becomes tuple
print(dimensions)
print(type(dimensions))

#Sets --> A set is a unique collection (removes duplicates)
# A Set is an Unordered,Unindexed,Mutable collection
ids = set() #empty set
print(ids)
ids = set([123,134,135,123])
print(ids)

courses = {'PFS','JFS','DA'}
print(courses)
print(type(courses))
print(courses[0]) # as set is unordered there is no index

#Dictionaries --> A dictionary(mapping object) is a collection of
#key value pairs ---> dict = {k:v},we access only by keys (indexed by keys)
#Dictionary is also mutable collection

details = {'branch':'vizag',
           'batches' :['PFS-VSP-007','PFS-VSP-006',
                       'PFS-VSP-005','PFS-VSP-004'],
           'course' :'PFS',
           'count':19}

print(details)
print(type(details))
print(len(details))
print(details['batches'])#we access by giving only key

#Every built-in Datatype is a built-in function
#int,float,complex,bool,str,list,tuple,set,dict
#Lists ---> tuples,sets,dict,str
marks = [35,24,54]
a = tuple(marks)
print(a)
b = set(marks)
print(b)
#c = str(marks)# it makes every symbol as a character
#print(c)
#print(len(c))

names= ('vinay', 'ram','raju')
print(names)

marks = [35,24,54]
#d = dict(marks) # its not possible like this
e = dict.fromkeys(marks) #we need to use fromkeys(),what ever
#elements we have taken will become keys and values will be none
print(e)

#tuple --->lists,set,str,dict
#set ---->list,tuple,str,dict

#Dictionaries ---> lists,tuples,sets
ids = {1:123,2:124}
a = list(ids) #it will only fetch keys
print(a)
b = tuple(ids)
print(b)
c = set(ids)
print(c)
d = str(ids)# Every symbol/object will be a character
print(d)
print(len(d))

names= ('vinay', 'ram','raju')
a = set(names)
print(a)

b = list(names)
print(b)

#Frozensets ---> It is an immutable set
a = frozenset((12,32,32,12))
print(a)
print(type(a))
print(len(a))

b = list(a)
print(b)

c = tuple(a)
d = set(a)
e = dict.fromkeys(a)
f = str(a)
print(c,d,e,f)
print(len(f))

d = 'vinay sambana'
e = list(d)
f = tuple(d)
g = set(d)
h = dict.fromkeys(d)
print(e,f,g,h)
'''
#Operators --> Arithemetic operators,Assigniment,Comparision,
#Logical,Membership,Identity,Bitwise Operators

#Arithemetic---> +,-,*,/(float division),//(Floor division)
#Quotient % Modulus(remainder),**(Exponential)
a = 3
b = 2
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)



































































 

























