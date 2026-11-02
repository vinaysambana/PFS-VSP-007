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
'''
























    
























