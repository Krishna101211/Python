'''
#1---------------------
s=eval(input())

if s.isupper():
    print("it is upper ",s)
elif s.islower():
    print("it is lower ", s)
elif s.isalnum():
    print("It only digit ",s)

#2-----------------------
s=eval(input())
if type(s)==str:
    print(len(s))
elif type(s)==list:
    s.pop()
    print(s)
elif type(s)==tuple:
    x=s[::-1]
    print(x)
else:
    print("invalid data type ")

#---------------------------------
#3 find largest among all variables
x=340
y=45
z=30

if x>y and x>z:
    print(f"{x} is greater than {y} and {z}")
elif y>x and y>z:
    print(f"{y} is greater than {x} and {z}")
elif z>x and z>y:
    print(f"{z} is greater than {x} and {y}")
else:
    print(" all are equal")


#4
age=eval(input("Enter age:"))

if 0<age<=17:
    print("child marriage")
elif age==18:
    print("Perfect age for marriage ")
elif 18<age<=30:
    print("Love marriage")
elif 30<age<45:
    print("Arrange marriage")
else:
    print("No marriage")

#5
x=eval(input("enter no:"))
y=['Mon','Tue','Wed','Thus','Fri','Sat','Sun']

if x==1:
    print(y[0])
elif x==2:
    print(y[1])
elif x==3:
    print(y[2])
elif x==4:
    print(y[3])
elif x==5:
    print(y[4])
elif x==6:
    print(y[5])
elif x==7:
    print(y[6])
else:
    print("Only accept number between 1to7")

#6 Pattern checker
s=eval(input("enter a string:"))
v="aeiou"
if s[0] in v:
    print("Starts with vowel ")
elif s[-1].isalnum():
    print("ends with digit")
elif s.islower():
    print("all are lowercase")
else:
    print("Random input")

#7 Fine calculator
x=eval(input("Enter speed:"))
if x<=60:
    print("no fine")
elif 61<x<=80:
    print("$200")
elif 81<=x<=100:
    print("$500")
elif 100==x:
    print("$1000")

#8 Recharge plan selector
x=eval(input("Enter plan id:"))
if x==1:
    print("")


#9 tempreature Checker
x=eval(input("Enter the temp:"))

if x<0:
    print("Freezing")
elif 0<x<15:
    print("Cold")
elif 16<x<30:
    print("Moderate")
else:
    print("Hot")

#10 Ticket price
x=eval(input("Enter Age to find ticket price:"))

if x<5:
    print("Free")
elif 5<=x<=18:
    print("$100")
elif 19<x<60:
    print("$200")
else:
    print("120")

# 7. Number Range Checker
number = int(input("Enter a number: "))
if 50 <= number <= 100:
    print("Within range")
else:
    print("Out of range")

# 8. Check Password Match
password = input("Enter password: ")
confirm_password = input("Confirm password: ")
if password == confirm_password:
    print("Login successful")
else:
    print("Incorrect password")

# 9. Student Fee Due
fee_status = input("Have you paid your fees? (yes/no): ").lower()
if fee_status == "yes":
    print("Access granted")
else:
    print("Please pay your fees")

# 10. Bus Ticket Eligibility (Age Check)
age = int(input("Enter your age: "))
if age < 5 or age > 60:
    print("Free ride")
else:
    print("Ticket required")

# 11. Check If Name Contains 'a'
name = input("Enter your name: ")
if 'a' in name.lower():
    print("Contains 'a'")
else:
    print("No 'a' found")

# 12. Online Exam Access Check
internet_status = input("Is your internet connected? (yes/no): ").lower()
if internet_status == "yes":
    print("Start Exam")
else:
    print("No Internet Connection")

# 13. Temperature Alert
temperature = float(input("Enter current temperature (°C): "))
if temperature > 35:
    print("Heat Alert")
else:
    print("Normal weather")

# 14. Check Minimum Balance
balance = float(input("Enter your bank balance: "))
if balance < 1000:
    print("Low balance warning")
else:
    print("Sufficient balance")

'''