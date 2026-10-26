'''
Sets---> A Set is an unordered,unindexed collection,allow unique values,heterogenous collection,mutable collection

#A set can contain only tuples in it but not lists,sets
we can use set() or data inside{} braces

#Every built-in datatypes is a built-in function
#subjects = {} #by default it will be empty dictionary
subjects = set()
print(type(subjects))
print(len(subjects))

data = ('Python','Aptitude','SQL','SS')
subjects = set(data)
print(subjects)
print(len(subjects))

ids = {123,125,126,129,['poll',123]}#TypeError


#Set Properties --->Membership
print(123 in {124,123,125})
ids = {123,121,125}
new_ids = {126,127}
#total = ids  + new_ids #TypeError
#print(total)
'''
#Set is a Mutable collection --->Methods ---> Insertion,Deletion along
#with Mathematical set operators
#add() ---> inserts single element to the set (unique values)
marks = {45,25,35,20,21}
'''
print(type(marks))
print(len(marks))
marks.add(250)
print(marks)
print(len(marks))
marks.add((12,13,15))
print(marks)
print(len(marks))
d_marks = [10,5,3,4,6]
marks.update(d_marks)# updates the set within itself or can take other sequence
print(marks)
print(len(marks))
marks.update("codegnan")
print(marks)
print(len(marks))
marks.add("vizag")
print(marks)
print(len(marks))

#marks.update(1,2,34)#TypeError

#remove(),discard(),pop()
print(marks.remove(45))
print(marks)

#print(marks.remove(4))#remove will remove the object if existing else raises KeyError

#discard() removes ana element from the set if existing if not it overrides the Error
print(marks.discard(45))
print(marks)

print(marks.discard(123456789))

marks.discard(20)
print(marks)

#pop() will removes and returns an arbitrary element from the set
#print(marks.pop())
#print(marks.pop())
#print(marks.pop())
#print(marks.pop()) #returns KeyError as set has become empty


#clear() removes all elements and returns an empty set
marks.clear()
print(marks)
'''


#Mathematical set operations ---> union(),intersection(),difference()......

a1 = {12,34,23,45}
a2 = {3,45,23,12}
'''
a3 = a1.union(a2)
print(a3)
print(len(a3))

a4 = a1 | a2 #returns the combined unique elements
print(a4)

a5 = a1.intersection(a2)# returns the common elements in both sets
print(a5)
print(len(a5))

a6 = a2 & a1
print(a6)
print(len(a6))

a7 = a1.difference(a2)#removes common elements from both sets
#and returns elemts from first set
print(a7)
print(len(a7))
a8 = a2 - a1 # - is a set difference operation
print(a8)
a9 = a1.symmetric_difference(a2) #removes common elements from both sets
#and returns all remaining elements
print(a9)

a10 = a2 ^ a1
print(a10)

#intersection_update()---> performs intersection and updates the first set
a3 = a1.intersection_update(a2)
print(a3)
print(a1)

# difference_update(),symmetric_difference_update()

a4 = a1.difference_update(a2)
print(a4)
print(a1)

a5 = a1.symmetric_difference_update(a2)
print(a5)
print(a1)


print(a1,a2)
a1.add(3)
print(a1,a2)

print(a1.issuperset(a2))
print(a2.issubset(a1))
print(a1.isdisjoint(a2))#returns True only when both sets have NULL intersection

#Dictionaries : A Dictionary is a collection of key,value pairs,we use
{k:v} as syntax,keys must be Unique,Mutable,Ordered,Indexed through keys
keys can be strings,numbers(int,float)

data = {1:'vinay',
        2:'vijay',
        3:'ajay'}
print(data)
print(type(data))
print(len(data))
print(data[2])
print(type(data[1]))
'''

#Dictionaries are Mutable collections
details = {'ids':['CGVI0242','CGVI0249','CGVI0224','CGVI0240'],
           'names':['Nikitha','Deepthi','Vinay','Tej'],
           'batches':'PFS-VSP-007','JFS-VIJWD-008','DA-HYD-009','CX-BNGLR-006',
           'place':('Vsp','Vijwda','Hyd','Bnglr'),
           'subjects':{'Python','Aptitude','Softskills','SQL'}}
'''
print(details)
print(len(details))
print(details.keys())
print(details['ids'])
print(type(details['ids']))
details['ids'].append("CGVI0245")
print(details['ids'])
details['ids'].insert(3,"CGVI0247")
print(details['ids'])
print(details['ids'][:3])#returns First 3 ids
print(details['ids'][::2])
'''
#Task :# 1)Insert Raju at the end also Sanju and Nihanth at the end in names
       # 2)Update subjects with SQL,Flask,FastAPI
       # 3)remove Bnglr and Vizag from place
       # 4)Convert batch number to lowercase

#1. Insert Raju, Sanju and Nihanth at the end of names
details['names'].append('Raju')
details['names'].append('Sanju')
details['names'].append('Nihanth')

# 2. Update subjects with SQL, Flask and FastAPI
details['subjects'] = {'SQL', 'Flask', 'FastAPI'}

# 3. Remove Bnglr and Vijwda from place
details['place'].remove('Bnglr')
details['place'].remove('Vsp')

# 4. Convert batch numbers to lowercase
details['batches'] = [batches.lower() for batches in details['batches']]

# Print the updated dictionary
print(details)



