'''
x=eval(input())

if isinstance(x,str):
    print(len(x))
    if x.isupper():
        print(x.upper())
    else:
        print("Already in upper case")
else:
    print(f" Given data not string")


x=eval(input())
if isinstance(x,list):
    options=input("Select options from 1,2,3")

    if  options==1:
        x.pop()
        print(x)
    elif options==2:
        print(x.sort())
    elif options==3:
        print(x.clear())
    else:
        print("Option is invalid")

else:
    print(f"{x} is not list")

#to book a ticket in book my show
print("Welcome to book  my show")
x=eval(input("Enter theater name:"))
theater = ['MAX','IMAX','IONAX']
movies = ['Last','Ayush ki love story']
price = [1000,2000,3000]

if x in theater:
    print(f"Movies availabel currently{movies}")
    m=input("User Movies:")
    if
else:
    print("Please Enter theater name from ",theater)

x=eval(input())
if x%2==1:
    print("Number is odd no.")
    if x%7==0:
        print("Number is divided by both 7 but not 2")
    else:
        print("Number is not divide by 7")
else:
    print("Number is even number")



d={'Python':'Python masters'}
x=eval(input("Please enter username:"))

if x in d.keys():
    print("Username is valid")
    y=eval(input("please enter Passsword:"))
    if y in d.values():
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Username is not valid")
#6 find middle element is odd or even
s=[3,4,6,8,9,1,8]
m=len(s)//2
print(m)
print(s[m])
if s[m]%2==0:
    print(f"{s[m]} is even ")
else:
    print(f"{s[m]} is odd")


#7 purchase a phone from shopping app
apps=["flipkart","amazon"]
categories=["electronics",'mobile','fashion','furniture']
x=input(f"Enter app name\n{apps} :")
if x in apps:
    print(f"following are available products \n{categories}")
    y=input("Please enter the category:")
    if y in categories:
        print("Product is confirmed")
    else:
        print("Select valid product ")
else:
    print(f"Please enter app name from{apps}")
'''
#8 wap
#credit=["axis",'bajaj','SBI']
payment_Method=['credit','debit','cod']
x=eval((input("Please tell your purchasing method:")))
if x in payment_Method:
    y=eval(input("Select quantity of product:"))
    if y>=3:
        #z=eval(input("please enter each product price:"))
        q=eval(input("1st product price:"))
        if q>500:
            print("Product satisfies price criteria")
            w= eval(input("2nd product price:"))
            if w> 500:
                print("Product satisfies price criteria")
                e = eval(input("3st product price:"))
                if e> 500:
                    print("Product satisfies price criteria")
                    print("congrats you unlock 40% discount")

                else:
                    print("Each product price greater than 500")

            else:
                print("Each product price greater than 500")

        else:
            print("Each product price greater than 500")
    else:
        print("Please select 3 or more than 3 product to unlock offer")
else:
    print(f"please choose purchasing method from:\n{payment_Method}")