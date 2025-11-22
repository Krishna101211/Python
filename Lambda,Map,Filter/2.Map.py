"""
Syntax-------->
def function name(Parameter):
    return parameter expression
new var= map(function_name,iterable)
print(list(new var))
"""
from importlib.resources import read_text


'''
s=[10,20,30,40,50]
def Square(s):
    l=[]
    for i in s:
        l.append(i**2)
    print(l)
Square([10,20,30,40,50])

print("-------------------------- Map Program")


def NEW_ONE(i):
    return (i**2)
x=map(NEW_ONE,[10,20,30,40,50])
print(x)  #<map object at 0x0000016D5239B100>
print(list(x))

print("************************")

w=lambda q:q**2
print(list(map(w,[10,20,30,40,50])))
'''

'''
d=[1,3,6,-7,-9,-10,-11,100,300,500]

def FUN(d):
    y=[]
    for i in d:
        if i>0:
            y.append(i)
    print(y)
FUN([1,3,6,-7,-9,-10,-11,100,300,500])

print("--------------------------------------------------------")

def FUN2(i):
    return i>0
x=map(FUN2,[1,3,6,-7,-9,-10,-11,100,300,500])
print(list(x))


print("*******************************************")

q=lambda e:e>0
print(list(map(q,[1,3,6,-7,-9,-10,-11,100,300,500])))

'''
'''
k=["good","bad","day's","yellow","red","blue","dark"]

r=lambda i:len(i)%2==0
print(list(map(r,["good","bad","day's","yellow","red","blue","dark"])))

print("*******************************************************")
def Length(u):
    return len(u)%2==0
m=map(Length,["good","bad","day's","yellow","red","blue","dark"])
print(list(m))
'''
"""
#wap to cube of the number
num=[1,2,3,4,5]
def cube(k):
    return k**3
l=map(cube,[1,2,3,4,5])
print(list(l))

k=lambda z:z**3
print(list(map(k,[1,2,3,4,5])))


#wap to merge two list
a=[1,2,3]
b=[4,5,6]
def merge(k,s):
    return k+s
l=map(merge,[1,2,3],[4,5,6])
print(list(l))

z=lambda o,p:o+p
print(list(map(z,[1,2,3],[4,5,6])))


#wap to convert number to string
x=[10,20,30,40]

def string(l):
    return str(l)
k=map(string,[10,20,30,40])
print(list(k))

o=lambda p:str(p)
print(list(map(o,[10,20,30,40])))

#wap to print the length of the word
words=["Python","map","example","students"]

def length(k):
    return len(k)
z=map(length,["Python","map","example","students"])
print(list(z))

o=lambda l:len(l)
print(list(map(o,["Python","map","example","students"])))

#wap to capitalize the word
words=["apple","banana","cherry"]
def capital(k):
    return k.capitalize()
o=map(capital,["apple","banana","cherry"])
print(list(o))

l= lambda p:p.capitalize()
print(list(map(l,["apple","banana","cherry"])))

#wap to find check even and odd
num=[1,2,3,4,5,6]
def even(k):
    return k%2==0

k=map(even,[1,2,3,4,5,6])
print(list(k))

p=lambda k:k%2==0
print(list(map(p,[1,2,3,4,5,6])))

#Absolute values
# x=[-5,-2,0,3,7]
# def absloute(k):
#     return abs(k)

#Concatenate strings with "*"
words = ["Hi", "Hello", "Python"]
def connect(k):
    return k+"*"

x=map(connect,["Hi", "Hello", "Python"])
print(list(x))

o=lambda k:k+'*'
print(list(map(o,["Hi", "Hello", "Python"])))

#Strip spaces from strings
words = ["  python ", " map ", " function  "]

def connect(k):
    return k.strip(" ")

x = map(connect, ["  python ", " map ", " function  "])
print(list(x))

o=lambda k:k.strip(" ")
print(list(map(o,["  python ", " map ", " function  "])))
"""
# #Check palindrome words
# words = ["mom", "python", "dad", "level"]


# #Convert floats to integers
# nums = [1.2, 3.7, 5.9]
# nums = [1.2, 3.7, 5.9]
# x= lambda i:int(i)
# print(list(map(x,nums)))

# #wap to return list of name and length pair
# n=['laptop','mouse','board','house','week']
#n=['laptop','mouse','board','house','week']
# x = lambda i: (i, len(i))
# print(list(map(x,n)))

#wap to return if the key is individual return its values else
# return its type
# s={10:"ten","hai":"value",(1,2,3):"collection",1.2:"decimal"}
#
# l= lambda i:s[i] if isinstance(i,(int,float,complex,bool)) else type(i)
# print(list(map(l,{10:"ten","hai":"value",(1,2,3):"collection",1.2:"decimal"})))



"""
# # 14.Given a list of dates in string format
# (["2025-09-18", "2024-12-31"]), use map() to extract only the year.
s=["2025-09-18", "2024-12-31"]
k=lambda i:i.split("-")[1]
print(list(map(k,["2025-09-18", "2024-12-31"])))
"""


"""
# # 15.Use map() with lambda and str.join() to join characters of each list into a string.
data = [["p", "y", "t", "h", "o", "n"], ["m", "a", "p"]]
# Output: ['python', 'map']
k=lambda i:''.join(i)
print(list(map(k,[["p", "y", "t", "h", "o", "n"], ["m", "a", "p"]])))
"""