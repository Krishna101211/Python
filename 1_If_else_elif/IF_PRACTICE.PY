'''
#wap to check the given data type is list
x=[1,2,3,4]
if type(x)==list:
    print(f'The given data is {x} is a list data type')
#            OR
if isinstance(x,list):
    print(f'The given data is {x} is a list data type')
'''

''' 
#wap to check the given character is part of the string 
s="evening" 
char="v" 
if char in s: 
    print(f'The given {char} is a part of the string') 

#wap to check the given string is odd length reverse the string 
x="webtech" 

if len(x)%2==1: 
    print(f'the given string is odd length {x[::-1]}') 

#wap to check first later start with upper case 
s="Python" 
if s[-1].isupper(): 
    print(f'in the given {s} first later start with upper case') 

#wap to check in the given string last character endswith vowels 
s="india" 
if s[-1] in "aeiouAEIOU": 
    print(f'in the given string last character is a vowel {s}') 

#wap to check the given number is odd 
s=11 
if s%2==1: 
    print(f'The given number  {s} is odd') 

if s%2!=0: 
    print(f'The given number  {s} is odd') 

#wap to check the given number is even without using % operator 
m=10 
if (m//2)*2==m: 
    print(f'The given {m} is  a even number') 

##wap to check the given number is even without using % operator 
n=20  #'0b10100' 

if (n&1)==0: 
    print(f'The given {n} is  a even number') 

n1=21 
if (n1&1)==1: 
    print(f'The given {n1} is  a odd number') 
'''
''' 
#wap to check the given number is digit 
s='92345678909876543' 
if s.isdigit(): 
    print(f'The given number {s} is digit') 
#           OR 

s1="4" 
if ord("0")<=ord(s1)<=ord("9"): 
    print(f'The given number {s1} is digit') 

#wap to check the given number is +ve 
s=eval(input("enter the number---->")) 
if s>0: 
    print(f'The given number {s} is a +ve') 
##wap to check the given number is +ve 
s1=eval(input("enter the number---->")) 
if s1<0: 
    print(f'The given number {s1} is a -ve') 
'''
''' 
#wap to check the given character is lower case then convert to upper case 
s="d" 
if s.islower(): 
    print(s.upper()) 
#                   OR 
if ord("a")<=ord(s)<=ord("z"): 
    print(chr(ord(s)-32)) 

#wap to check the given character is upper case then convert to lower case 
x="A" 
if ord("A")<=ord(x)<=ord("Z"): 
    print(chr(ord(x)+32)) 
#           OR 
if x.isupper(): 
    print(x.lower()) 
'''

''' 
#wap to check the given number is odd then store into list 
y=11 
#[11] 
x=[] 
if y%2==1: 
    x.append(y) 
    print(x) 

k=[] 
if y%2==1: 
    k=k+[y] 
    print(k) 

#wap to check the given number is even typecasting to complex 
s=901 
if s%2==0: 
    print(complex(s)) 
'''


#---------MY prep ---------------------------------------------------------------------------------
'''
x=int(input())
if x>0: 
    print(f"Given number {x} is positive ")
#same format for -ve check just x<0
#same format for -ve check just x==0


x=int(input())
if x%5==0:
    print(f"Given number {x} is divisible by 5 ")


x=100
if x<=100:
    print(f"Given number {x} is less than 100")


x=(input())
if len(x)==3:
    print(f"{x}  given number  is 3 digit ")

x="Mllo"
if ord(x[0]) > 65 and ord(x[0])<90:
    print(f"{x} is upper letter")

x= 'Mllo.'
if x.endswith('.'):
    print(f"{x} ends with .")

s='apple'
if 'p' in s:
    print("a is present")

x='level'
if x[0].startswith(x[-1]):
    print("correct")

x=[2,4,5,4]
if x[-1]%2==0:
    print(f"{x[-1]} present even number")

lst = [5, 5, 9]
if lst[0]==lst[1]:
    print(f"{lst} first two elements are same ")

y = [50, 40,30]
if sum(y)>=100:
    print(f'{y} sum greater than 100' )

year=2024
if year%4==0:
    print(f"{year} it is leap year ")

file='smile.txt'
if file.endswith('.txt'):
    print(f"give {file} is in text format")

num = 42
if num%3==0 and num%7==0:
    print(f" {num} is divisible by 3 and 7")

cc='1234567812345678'
if len(cc)==16 and cc.isalnum():
    print(f" {cc} have 18 numbers and all are numbers")

#29
score=int(input())
if score==70:
    print("Good Luck")

#34
s=input()
if s[-1::-1]==s[0::1]:
    print(f"{s} is palindrome ")

#38
lst=[]
s=int(input())
if s%2==0:
    lst.append(s)
    print(f" {lst} contain even number ")

#39
x=int(input())
if 40<=x<=200 and x%4==0 :
    y=ord(str(x))
    print(f"{x} AScii {y} and divisible by 4")

#40
a=eval(input("enter number"))
x={}
if a.isaplpha():
    x.update({a:ord(a)})
    print(x)
#41
d={}
x='HII'
if x.isupper():
    y=x.lower()
    d.update({[y]:ord(y)})
    print(d)
'''