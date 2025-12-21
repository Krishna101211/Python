"""
CHARACTERS CLASSES PATTERN IN REGULAR EXPRESSION
***************************************************
1)[abc]--->Either a or b or c
2)[^abc]--->Except a and b and c
3)[a-z]---->any lower case alphabet symbol
4)[A-Z]---->Any upper case alphabet symbol
5)[a-zA-Z]--->any alphabet symbol
6)[0-9]--->any digit from 0 to 9
7)[a-zA-Z0-9]--->Any alphanumeric characters
8)[^a-zA-Z0-9]--->except alphanumeric characters(special characters)
Predefined Characters Classes
---------------------------------
9)\s----->space characters
10)\S----->Any characters except space characters
11)\d---->Any digit from 0 to 9
12)\D---->Any characters except digit
13)\w----->Any word characters [a-zA-Z0-9]
14)\W----->Any characters except word characters (special characters)
15).---->Any characters including special characters
16)^---->Pattern should be at the beginning
17)$---->Pattern should be at the end
18)+ --->group of characters(matches 1 or any number of occurance of the preceding characters)

"""
import re

"""
findall()
#new_var_name=re.findall("Pattern",source_of_string)
"""

s = "welCOME to ALL 2025"
'''
w=re.findall('[a-z]',s)
print(w)

w1=re.findall('[a-z]+',s)
print(w1)

w2=re.findall('[A-Z]',s)
print(w2)

w2=re.findall('[A-Z]+',s)
print(w2)

w3=re.findall('[A-Za-z]',s)
print(w3)

w4=re.findall('[0-9]',s)
print(w4)

w4=re.findall('[0-9]+',s)
print(w4)

w5=re.findall(r'\d',s)
print(w5)

w5=re.findall(r'\d+',s)
print(w5)
'''

d = "Python and POWER APPS CLASS  in the Month of 1282025 @#$%^&*(*&^"
'''
e=re.findall('[POWER]+',d)
print(e)

e1=re.findall('[^POWER]+',d)
print(e1)

e2=re.findall('[^A-Za-z0-9]',d)
print(e2)
print()
e3=re.findall("\W",d)
print(e3)
print()
e4=re.findall("\w+",d)
print(e4)

e5=re.findall("\s",d)
print(e5)

print()

e6=re.findall(" ",d)
print(e6)

print()

e7=re.findall("\S+",d)
print(e7)

'''

x = "Python Subject"

# startswith-->^
y = re.findall("^Python", x)
print(y)  # ['Python']

y1 = re.findall("^ython", x)
print(y1)  # []

# endswith--->$

y2 = re.findall("$Subject", x)
print(y2)  # []

y3 = re.findall("Subject$", x)
print(y3)  # ['Subject']



import re

# match()
"""
match()
syntax:---> new_var_name=re.match("Pattern",source_of_string)

examples:---->
s="Python class"
w=re.match("Pyt",s)
print(w)
print(w.start())
print(w.end())
print(http://w.group())

print("------> new code---->")
w1=re.match("class",s)
print(w1)

print("*****************")

w2=re.match("hon",s)
print(w2)

print("#############")
w3=re.match("yth",s)
print(w3)

"""
"""
#Fullmatch()
syntax:--> new_var_name=re.fullmatch("Pattern",source_of_string)

s="Python class"
a=re.fullmatch("Python class",s)
print(a)
print(a.start())
print(a.end())
print(http://a.group())

print("new example---->")

b=re.fullmatch("Python cla",s)
print(b)

print("new--one")
c=re.fullmatch("Pyt class",s)
print(c)

print("last--one")
d=re.fullmatch("thon class",s)
print(d)

s="Python class"
d=re.fullmatch("python class",s)
print(d)
"""

"""
search()
syntax:---> new_var_name=http://re.search("Pattern",soure_of-string)

x="welcome to all"
http://y=re.search("o",x)
print(y)
print(y.start())
print(y.end())
print(http://y.group())

print("*************")
x="welcome to all"
http://z=re.search("w",x)
print(z)

print("$$$$$$$$$$$$$$")
x="welcome to all"
http://n=re.search("x",x)
print(n)

print("@@@@@@@@@")
x="welcome to all"
http://q=re.search("come",x)
print(q)
print(q.start())
print(q.end())
print(http://q.group())

"""

"""
finditer()

#syntax:--> new_var_name=re.finditer("Pattern",soure_of-string)

s="good afternoon guys welcome to all"
a=re.finditer("o",s)
print(a)  #<callable_iterator object at 0x000001C357645DE0>

print(list(a)) #typecasting
#
for i in a:  #looping
    print("o------>",i)

s="good afternoon guys welcome to all"
a=re.finditer("x",s)
print(list(a))

"""

"""
sub()

#syntax:-->new_var_name=re.sub("old_Pattern","new_Pattern",soure_of_string,count)


subn()
#syntax:-->new_var_name=re.subn("Pattern","newPattern",soure_of_string,count)

"""

d = "Programming"
# syntax:-->new_var_name=re.sub("old_Pattern","new_Pattern",soure_of_string,count)

e = re.sub("g", "*", d, 1000)
print(e)

print()

e1 = re.subn("g", "*", d, 1000)
print(e1)



"""
 REGULAR EXPRESSION EXAMPLE

#1.matches any number between 0-9
a="The cost of the book is Rs.100"


#2.matches only lower case letter and upper case letter
b="hello HOW ARE YOU"



#3.write a program to count the number of white space in a given string
c="HELLO world welcome to python Hi how are you. Hi how are you"



#4.sum all the numbers in the below string
word="PYTHON12nREG567exp2"



#5.matches everything apart from numbers between 0-9
a="The cost of the book is Rs.100"



#6.matches everything apart from "a","b","c","d"
b="abcdefghijklmnop"



#7.matches only numbers
word="@hello12world34welcome!123"



#8.extracting file with extension
s="Downloading http://archive.zip file to download folder python http://hero.py
 and afternoon.txt and slicing.jpeg"




"""


# 4.sum all the numbers in the below string
word = "PYTHON12nREG567exp2"
num = re.findall('[0-9]', word)
print(num)  # ['1', '2', '5', '6', '7', '2']  #23

total_sum = 0
for i in num:
    total_sum = total_sum + int(i)
print(total_sum)  # 23
x="Downloading http://archive.zip file to download folder python http://hero.py and afternoon.txt and slicing.jpeg"

q=re.findall('[A-Za-z]+\.[A-Za-z]+',x)
print(q)


import re

#findall():----> var_name=re.findall("Pattern",source_of_string)

x="wel COME To ALL 1234 @#$ -- PYTHON vs JAVA ^&*() 2345"

'''
y=re.findall('[a-z]',x)
print(y)

y1=re.findall('[A-Z]',x)
print(y1)

y2=re.findall('[0-9]',x)
print(y2)

y3=re.findall('[A-Za-z0-9]',x)
print(y3)

y4=re.findall(r'\d+',x)
print(y4)

y5=re.findall(r'\D',x)
print(y5)

y6=re.findall(r'\w',x)
print(y6)

print()

y7=re.findall(r'\W',x)
print(y7)

y8=re.findall(" ",x)
print(y8)
print(len(y8))

print()

y9=re.findall(r'\s',x)
print(y9)
print(len(y9))

print()

y10=re.findall(r'\S',x)
print(y10)

'''
'''
d="ABCDEFGHIJ"
r=re.findall('[^ABC]',d)
print(r)
print()
r1=re.findall('[ABC]',d)
print(r1)
'''

'''
t="wel come"
startswith--->^
u=re.findall("^wel",t)
print(u)
print()

u1=re.findall("^come",t)
print(u1)
ends with--->$

u2=re.findall("come$",t)
print(u2)

u3=re.findall("wel$",t)
print(u3)
'''
'''
e='http://www.facebook.com'

w=re.findall(r"\D+",e)
print(w)

w1=re.findall(r"\S+",e)
print(w1)

w2=re.findall('[A-Za-z.]+',e)
print(w2)

w3=re.findall(".+",e)
print(w3)

d="http://python.py and JAVA.JVM and webtech.xml"
w=re.findall('[A-Za-z]+\.[A-Za-z]+',d)
print(w)
'''

word="PYTHON12nREG567exp2"
u=re.findall('[0-9]',word)
sum=0
for i in u:
    sum=sum+int(i)
print(sum)  #23

file_format=["Graphic Interchange Format",
              "Advanced Audio Coding",
            "HyperText Markup Language",
             "Content Management System",
            "Windows Media,Audio",
            "Comma Separated Values"]

for i in file_format:
    x=re.findall('[A-Z]',i)
    print("".join(x))


