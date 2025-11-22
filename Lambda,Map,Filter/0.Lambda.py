"""
                    lambda syntax
syntax1
new_var_name=lambda arg1,arg2,arg3........:expression
print(new_var_name)  #object address
print(new_var_name(value1,value2......))

syntax2:->
new_one=lambda arg1 :TSB if condition else block
print(new_one())

syntax3:-->
new_one=lambda arg1.... :[expression for loop condition]

"""
from os.path import split

from setuptools.command.build_ext import if_dl

'''
def spam():
    print("evening")
print(spam) #<function spam at 0x0000026A522E4AE0>
spam()


x=lambda :"evening"
print(x)  #<function <lambda> at 0x000001A6C469F9C0>
print(x())


y=lambda i,j:i*j
print(y(4,5))
'''

# s=25
'''
# syntax2:->
# new_one=lambda arg1 :TSB if condition else block
# print(new_one())
'''
# a=lambda s:f'The given number {s} is a even number ' if s%2==0 else f'The given number {s} is a odd number '
# print(a(25))
# print(a(22))

# e=4
# d=lambda e:(e**2,e**3)
# print(d(4))


# w="Python"
# e=lambda w:(len(w),w)
# print(e("Python"))


# e1=lambda w:((len(w),w),{len(w):w})
# print(e1("Python"))



"""
# syntax3:-->
# new_one=lambda arg1.... :[expression for loop condition]
 """
# q=lambda k:[i[0] for i in k]
# print(q(["apple","iphone","mack"]))


# q1=lambda k:[i for i in enumerate(k)]
# print(q1(["apple","iphone","mack"]))


# q2=lambda k:[(i,j) for i,j in enumerate(k)]
# print(q2(["apple","iphone","mack"]))


# e=[10,15,17,18,29,30]
# for i in e:
#     if i%5==0:
#         print(i)
#     else:
#         print(i**2)


# r=lambda e:[i  for i in e if i%5==0]
# print(r([10,15,17,18,29,30]))

# r1=lambda e:[i if i%5==0 else i**2 for i in e]
# print(r1([10,15,17,18,29,30]))

# Lambda Example
# 1.add two numbers
# x= lambda a,b:a+b
# print(x(2,3))


# 2.multiply two numbers
# y= lambda i,j:i*j
# print(y(10,20))

# 3.find maximum of two numbers
# k = lambda a, b: max(a, b)
# print(k(10, 20))

# 4.find minimum of two numbers
# k= lambda i,j:min(i,j)
# print(k(10,20))

# 5.square of a numbers
# l= lambda j:j**2
# print(l(10))


# 6.cube of a numbers
# l= lambda j:j**3
# print(l(10))


# 7.check even number
# k=lambda l:print("even") if l%2==0 else print("not even")
# print(k(100))


# 8.Absolute value
# l=lambda k:print(abs(k))
# print(l(-20))


# 9.greater among three numbers(max())
# a=10
# b=20
# c=30
# j=lambda k,l,m:print(max(k,l,m))
# print(j(10,20,30))


# 10.length of a string
# k= lambda length_string:len(length_string)
# print(k("hello"))

# 11.Reverse a string
# reverse_string=lambda k:k[::-1]
# print(reverse_string("hiii"))

# 12.Palindrome check
# palindrome_check=lambda k:print("its palindrome") if k[::-1]==k else print("not palindrome")
# print((palindrome_check("mom")))

# 13.find largest word in a string
# s = "python is powerful"
# largest_word = lambda text: max(text.split(), key=len)
# print(largest_word(s))

'''
# 14.Last digit of a number
s = 789
last_digit = s % 10
print(last_digit)
'''

'''
# 15.First digit of a number
s = 789
while s >= 10:
    s //= 10
print(s)
'''

"""
# 16.Swap two numbers
a = 10
b = 20
swap = lambda x, y: (y, x)
a, b = swap(a, b)
print("a =", a)
print("b =", b)
"""

'''
# 17.Leap year check
s = 2024
leap = lambda y: "Leap Year" if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else "Not a Leap Year"
print(leap(s))
'''


# 18.String uppercase
# x="python"
# k= lambda l:l.upper()
# print(k(x))

'''
# 19.Title case string
y="hello world"
k = lambda l: [i.title() for i in l.split()]
print(k(y))
'''

# 20.Count words in a string
# s="python is great"
# l=lambda k:[print(len(i)) for i in k.split()]
# print(l(s))

# 21.wap to check the number is divisible by both 3 and 7
k= lambda j: [print("divisble by 3and7") if j%3==0 and j%7==0 else print("not divisble by 3and7")]
print(k(21))
# 22.Square root of a number


# 23.Rectangle area (length * width)
#
#
# http://24.Circle area (pi*r*r)
#
#
# 25.Concatenate two strings
#
#
# 26.Repeat string n times
#
#
# 27.Check substring present
#
#
# 28.Find the largest of four numbers(use max()function)
#
#
# 29.wap to return the key of a dictionary
# a={"hello":"Sony","How":"are","you":"bye"
#
#
# 30.wap which returns first element of a sequence
#
#
# 31.wap which returns length of any iterable
#
#
# 32.wap which returns the list of squares of numbers in a list
# l=[2,3,4,5,6]
#
#
# 33.wap to print the numbers present in a list with their corresponding indices pair
# l=[100,200,300,400,500]
#
#
# 34.wap to check a data is sequence if it is sequence then return length pair else type pair
#
#
# 35.wap to check even or odd,if it is even return square of that value else square root of that
# value
#
#
# 36.wap to check len of given string ,if length is even return as it is else return reverse
# of that string
#
#
# 37.wap to check length of given string and return value and length in tuple and dictionary
#
#
# 38.wap to check a data is sequence if it is sequence then return length pair else type pair
#
#
# 39.wap to return if no is divisible by 5 then increment with 5 else decrement with 5
#
#
# 40.Check if string is an anagram
# s="listen"
# s1="silent"
