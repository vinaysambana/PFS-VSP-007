'''
Task on Control statements
#Best Seller
number = int(input("Enter the no of sales:"))
if number > 1000:
    print("Best Seller")
else :
    print("No Output")


raining = bool(input("Enter the details"))
print(raining)
print(type(raining))
if raining :
    print("Extra Rain Charges Apllied")
else :
    print("No Output")

order_value = int(input("Enter the order_value:"))
print(order_value)
if order_value < 99 :
    print(f"Final Bill Amount:{order_value+30}")
else :
    print(f"Final Bill Amount:{order_value}")

budget = int(input("Enter the Amount"))
if budget>10000:
    print("Plan:Trip")
elif budget > 5000:
    print("Plan:Resort Stay")
elif budget > 3000:
    print("Movie and Dinner")
elif budget > 1000:
    print("Plan:Cafe and Shopping")
elif budget > 500:
    print("Plan:Street Food and Park Visit")
else:
    print("Plan:Stay Home")
'''

#Repitition Statements (Loops) ---> Loops helps us in automating repetitive
#tasks ---> for,while
#Usage of for : ---> It is used mainly to iterative within in lists,strings,
#ranges...

'''
Syntax :
for <temp> in collection/range
    statements(s)....
    .................
    .................


marks = [25,20,21,19,10,12]
#Marks can be dynamic
marks = list(map(int,input("Enter the marks:").split(',')))
for i in marks :
    print(i)# it traverse within the loop


#Calculate the total marks
marks = list(map(int,input("Enter the marks:").split(',')))
total = 0
for mark in marks:
    #print(i)
    #here we need to update total with each mark
    total = mark + total #total += mark
    print(total)
print(f'Total marks are :{total}')
print(f'Avg marks are : {total/len(marks)}')

subject = input("Enter the subject")
for i in subject:
    print(i)

details = {'ids':[121,123,125],
           'marks':[25,20,21]}
for data in details: #indexed through keys
    print(data)
    #print(details[data])#it returns values

for data in details.values():
    print(data)

for key,value in details.items():
    print(key,value)

for data in details:
    print(details[data])#it returns values

#range(start,stop) ---> u can mention start and stop postion (values)
#start is included,end is excluded
for i in range(1,11):
    print(i,i**2)
    print('<--->')

#range(start,stop,step)
for i in range(1,21,1):
    print(i)
for i in range(1,21,2):
    print(i)

#Get First 10 even numbers
for i in range(2,21,2):
    print(i)


#print numbers from 10 to 1 in reverse order
for i in range(10,0,-1):
    print(i)


#print 'A' to 'Z' in a single line # [chr(i) always digit,ord('s') always string]
for i in range(65,91):
    #print(i,chr(i))
    print(chr(i),end=' ')
'''

names = ['Akash','Kaushik','Vijay','Sanjay','Lokesh']
for name in names:
    print(name,end= ' ')#this returns in horizontal order

for i in range(len(names)):
    print(names[i]) # names[0] --->Akash--->names[1]--->Kaushik

#Ask integer input from user and get the sum of the numbers as per input
'''
Test-1:
4
10

Test-2:
6
21

Test-3:
-5
No Output


n = int(input("Enter a Number:"))
if n>=0:
    result = 0 #target
    for i in range(n+1):
        #print(i)
        result = result + i
    print(f'Result of {i} is {result}')
else:
    print("No Output")
'''

#Use Case : Checking daily workout app usage
work_log = [1,1,1,0,1,1,0]
#1 ---> workout done
#0 ---> workout missing
#Find the longest workout streak
work_log = [1, 1, 1, 0, 1, 1, 0]

longest_streak = 0 #target
current_streak = 0

for day in work_log:
    print(day)
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0
print(f'Longest work_log streak is {longest_streak}')
















