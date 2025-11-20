'''#wap progam eligliblity for marraige
M=int(input())
F=int(input())

if M>=21 and F>=18:
    print(" Male and Female is ready for marraige ")
else :
    print(" both are not ready for marraige ")

#2
n1=34
n2=54
if n1>n2:
    print(f"{n1} is  greater than {n2}")
else:
    print(f"{n1} is smaller than {n2}")

#3

x=eval(input())
if x%2==1:
    y=x+1
    print(f"{x} is odd number we make it {y} even")
else:
    print(f"{x} is  even")


#4
x="ello"
if x[0].isupper():
    print("given string has upper letter")
else:

    print(x.capitalize())
'''
'''
#5
x=eval(input())
if x%2==0:
    y=x/2
    print(f"{x} is odd number we make it {y} half value")
else:
    z=x**x
    print(f"{x} is  even")


#6
x=eval(input())
if x%3==0 and x%7==0 :
    print("number is divisble by 3 and 7 ")
else:
    print(f"{x} is  even")


#7
x=eval(input())
if x>0:
    print("number is +ve")
else:
    print("number is -ve")

#8
s="Python"
x=str(input())
if x in s:
    print(f"{x} present in string ")
else:
    print("not present in string ")



#9
D={'a':'apple'}
if len(D)%2==0:
    print("length of dict is even ")
else:
    D.update({"M":"Mango"})
    print(D)

#10
x=eval(input())#abs use to convert to -ve 
if x>5:
    y=-x
    print(f"{y}")
else:
    print(x)
'''
