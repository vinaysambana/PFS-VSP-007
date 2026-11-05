'''
while ---> initalized statement,counter..
'''
#banking scenario ---> Pin authentication if more than 3 attempts Account Locked
'''
pin ="2612"
max_attempts =3
#you need to have a current attempt
current_attempt=0
while current_attempt < max_attempts:
    enter_pin = input("enter the Atm pin:")
    if enter_pin == pin :
        print("login successfully")
        print("U have to withdraw the money")
        break
        #continue
    else:
        print("entered pin is incorrect")
        current_attempt +=1
else:
    print("account locked..try after the 24 hours")
'''
#BMI Scenario (Usecase) we will makeuse of control  block statements:

#BMI --->Body Mass index --> bmi = weight(kgs) /(height**2) (meters)
'''
Feet --->1 feet -->12 inches  ---> 2.54cm ---> 30.48cm
--->5 feet 6 inches --> 167.78 cms --> 1.67 meters
'''
'''
#print(bmi)
           #(<18.5 --> Underweight,18.5 -24.9 --> healthy,25-29.9 -->overweight  >=30---> obesity)
n = int(input("how many users:"))
for i in range(n):
       weight = int(input("enter weight in kgs:"))
       height = float(input("enter the height in meters:"))
       name=input("enter the name:")
       if weight > 0 and height > 0:
           bmi =(weight)/((height)**2)
           if bmi <18.5:
                     print(f"{name}---> you are under weight as BMI is {bmi}")
           elif bmi >=18.5 and bmi <=24.9:
                    print(f"{name}-----> you are in perfect physique,BMI is {bmi}")
           elif bmi >=25 and bmi <=29.9:
                    print(f"{name} ----> you are Overweight need to maintain diet {bmi}")
       else:
            print(f"enter only +ve values")
'''      
#Assert -->It is mainly used in debugging checking during development
#it tests whether a given condition is satisfied or not its
#a mandatory else it will raise error.It is mainly used to catch bugs by ensuring the conditions hold true...

#Syntax: assert <condition>,"Error Message"

x = int(input("enter the value:"))
assert x>0,"enter only positive value"
x=x**2
print(F"final result is {x}")
assert x in [24,25,12,10]
print(f"search found")
            
        
