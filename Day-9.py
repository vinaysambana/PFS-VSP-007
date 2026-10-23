'''
Sequences ---> Strings,Lists[],Tuples(),Sets set(),Dictionaries{}
Lists [] ---> A List is an Ordered,Mutable,Indexed and heterogenous collection
it will be dynamic in size
'''

#Creation of Lists
details = [123,"saketh",32,"PFS",75.5]
print(type(details))
print(len(details))
print(details)

#Nested Lists
batches = [["PFS","PFS-VSP-007","PFS-VSP-008"],
           ["DA","DA-VSP-007","DA-VSP-008"],"Vizag",8]
print(len(batches))
print(type(batches))

'''
#Indexing,Slicing,Striding
print(batches[0])
print(batches[-3])

print(batches[1:4]) #observe the output
print(batches[:2])

print(batches[1:5:2])
print(batches[0:4:1])
print(batches[0:0:3])

print(batches[-5:-1:4])
print(batches[-1:-5])


#Subindexing ---> Accessing index within the index of a collection(str,list,tuple

print(batches[0])
print(batches[0][1])
print(type(batches[2][2:]))
print(batches[0][1][4:7])
print(batches[0][1][4:7][::2])


print(batches[0][1][:3] + batches[0][1][7:])
print(batches[1][2])
print(batches[1][2][-3:])

#Lists supports Repetition,Merging and its also an Iterable (iterate through loops)

print(batches[0][1])
print(len(batches[0][1]))
print(batches[0][1][:3] + batches[0][1][-4:])

print([1,2,3]*3)   # Repetition
#print([1,2,3]+3)  # type Error
print([1,2,3] + batches) # Merging

a = [1,2,3]
b = a*3
print(len(b))

print('Vizag' in batches)#Membership
print('PFS' in batches) # it Returns False as in checks the elements present in the
#list but not the list inside the list(Nested List)
print('PFS' in batches[0])# Returns True
'''
#Lists Methods

data = []
#print(dir(data))#return list of all available methods
#append(),extend(),insert()
'''
#append()---> insert object to the end of the list
# will always increment the length by 1
# it will allows only 1 argument 
data.append(24)
print(data)

data.append('vizag')
print(data)

#data.append('Python','MSQL')#TypeError
data.append(["Python","MYSQL"])
print(data)
print(len(data))

marks = [20,25]
print(marks)
marks.append(23)
print(marks)
      
#extend()---> insert multiple elemnts(objects) to the end of the list
data.extend(['python','MYSQL'])
print(data.extend(['python','MYSQL']))

print(data)# in this case list length becomes 5 as we have inserted
#two objects from the iterable
data.extend('vizag')#check this
print(data)

#inser(index,object) ---> inserts elements before index

data.insert(2,'saketh')
print(data)

data.insert(-3,'codegnan')
print(data)

data.insert(2,[34,45,6])
print(data)

#Lists are Mutable
marks = [25,24,27,28,30,35,36]
print(marks)
marks[2] = 45
print(marks)
marks[:3] = ['saketh','codegnan','python']
print(marks)

#In above cases data is being modified in original list
#(Indexing case length remains constant but data is modified,
#Whereas in slicing case it may increase,decrease)


#pop(),remove(),clear() ---> Removes elements from the list
subjects = ['Python','Aptitude','SS','Flask']

#pop()---> removes by default last elements if index is not mentioned
#print(subjects.pop())#removes and returns last elements
#print(subjects.pop(2))
#print(subjects.pop(5))# raises IndexError
#print(subjects)

#remove()---> removes specific value from the collection(only first occurance)
subjects.remove("Python")
#print(subjects.remove("Python"))#returns None
#subjects.remove("codegnan") #ValueError

#clear() ---> removes all the elements from the list and returns empty list

subjects.clear()
print(subjects)


#index(),count()
#index(start)#returns only first occurance index position
marks = [24,25,24,26,27,30]
print(marks)
marks.index(24)
print(marks)

print(marks.index(24,1))#here we are exclusively giving start position
#print(marks.index(545)) #ValueError

#count()---> returns the count of occurances
print(marks.count(24))
print(marks.count(248))

#Task: Create a Nested Lists and Strings and Perform List methods
'''     






















