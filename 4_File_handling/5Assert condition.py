"""
assret condition
"""
'''
s=100
assert s<50,"number is greater than 50"
print(s)
'''

'''
def Number(x):
    assert isinstance(x,str)
    print("The given data is string")
Number("abcd")
# Number(1234)
'''
'''
w=eval(input("enter the data"))
assert w==w[::-1],"its a palindrome"
print(w)
'''

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

s=25
'''
syntax2:->
new_one=lambda arg1 :TSB if condition else block
print(new_one())
'''

'''
a=lambda s:f'The given number {s} is a even number ' if s%2==0 else f'The given number {s} is a odd number '
print(a(25))
print(a(22))


e=4
d=lambda e:(e**2,e**3)
print(d(4))

'''


w="Python"

e=lambda w:(len(w),w)
print(e("Python"))

e1=lambda w:((len(w),w),{len(w):w})
print(e1("Python"))


k=["apple","iphone","mack"]
"""
syntax3:-->
new_one=lambda arg1.... :[expression for loop condition]
"""
q=lambda k:[i[0] for i in k]
print(q(["apple","iphone","mack"]))

q1=lambda k:[i for i in enumerate(k)]
print(q1(["apple","iphone","mack"]))

q2=lambda k:[(i,j) for i,j in enumerate(k)]
print(q2(["apple","iphone","mack"]))

e=[10,15,17,18,29,30]
for i in e:
    if i%5==0:
        print(i)
    else:
        print(i**2)

r=lambda e:[i  for i in e if i%5==0]
print(r([10,15,17,18,29,30]))

r1=lambda e:[i if i%5==0 else i**2 for i in e]
print(r1([10,15,17,18,29,30]))


"""
Lambda Example

1.add two numbers


2.multiply two numbers


3.find maximum of two numbers


4.find minimum of two numbers


5.square of a numbers


6.cube of a numbers


7.check even number


8.Absolute value


9.greater among three numbers(max())
a=10
b=20
c=30


10.length of a string


11.Reverse a string


12.Palindrome check


13.find largest word in a string
s="python is powerful"


14.Last digit of a number
s=789


15.First digit of a number
s=789


16.Swap two numbers
a=10
b=20


17.Leap year check
s=2024


18.String uppercase
x="python"


19.Title case string
y="hello world"


20.Count words in a string
s="python is great"


21.wap to check the number is divisible by both 3 and 7


22.Square root of a number


23.Rectangle area (length * width)


http://24.Circle area (pi*r*r)


25.Concatenate two strings


26.Repeat string n times


27.Check substring present


28.Find the largest of four numbers(use max()function)


29.wap to return the key of a dictionary
a={"hello":"Sony","How":"are","you":"bye"


30.wap which returns first element of a sequence


31.wap which returns length of any iterable


32.wap which returns the list of squares of numbers in a list
l=[2,3,4,5,6]


33.wap to print the numbers present in a list with their corresponding indices pair
l=[100,200,300,400,500]


34.wap to check a data is sequence if it is sequence then return length pair else type pair


35.wap to check even or odd,if it is even return square of that value else square root of that
value


36.wap to check len of given string ,if length is even return as it is else return reverse
of that string


37.wap to check length of given string and return value and length in tuple and dictionary


38.wap to check a data is sequence if it is sequence then return length pair else type pair


39.wap to return if no is divisible by 5 then increment with 5 else decrement with 5


40.Check if string is an anagram
s="listen"
s1="silent"
"""