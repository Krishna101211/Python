"""
# 1.Filter even numbers
n=[1,2,3,4,5,6]
def even(i):
    return i%2==0
z=list(filter(even,[1,2,3,4,5,6]))
print(z)

x=lambda i:i%2==0
print(list(filter(x,[1,2,3,4,5,6])))

#2.filter odd numbers
y=[10,11,12,13,14]
def odd(i):
    return i%2==1
z=list(filter(odd,[1,2,3,4,5,6]))
print(z)

x=lambda i:i%2==0
print(list(filter(x,[1,2,3,4,5,6])))


#3.Remove empty strings
data=["apple","","banana","","cherry"]
def empty(i):
    return i not in " "
print(list(filter(empty,["apple","","banana","","cherry"])))

x=lambda i:i not in " "
print(list(filter(x,["apple","","banana","","cherry"])))

#4.Keep Positive numbers
z=[-5,-2,10,3,7]
def positive(i):
    return i>0
print(list(filter(positive,[-5,-2,10,3,7])))

x=lambda i:i>0
print(list(filter(x,[-5,-2,10,3,7])))


#5.Filter Truthy values
s=[0,False,"",None,"Hii",6]
def Truthy(i):
    return i!=False
print(list(filter(Truthy,[0,False,"",None,"Hii",6])))

x=lambda i:i!=False
print(list(filter(x,[0,False,"",None,"Hii",6])))


#6.Keep strings starting with “a”
words = ["apple", "banana", "avocado", "cherry"]
def start(i):
    return i.startswith("a")
print(list(filter(start,["apple", "banana", "avocado", "cherry"])))

x=lambda i:i.startswith("a")
print(list(filter(x,["apple", "banana", "avocado", "cherry"])))


#7.Keep only digits from a string
s="a1b2c3d4"
def dig(i):
    return i.isdigit()
print(list(filter(dig,"a1b2c3d4")))

x=lambda i:i.isdigit()
print(list(filter(x,"a1b2c3d4")))

# 8.Keep only alphabets from a string
s1= "p3y4t5h6o7n"
def dig(i):
    return i.isalpha()
print(list(filter(dig,"a1b2c3d4")))

x=lambda i:i.isalpha()
print(list(filter(x,"a1b2c3d4")))


#9.Filter students who passed (marks ≥ 50)
marks = {"Ann": 45, "Ben": 70, "Cat": 55}
def passed(i):
    return marks[i] >= 50
print(list(filter(passed ,{"Ann": 45, "Ben": 70, "Cat": 55})))

x=lambda i:marks[i] >= 50
print(list(filter(x,{"Ann": 45, "Ben": 70, "Cat": 55})))

#10.Keep numbers divisible by 3
nums = [3, 6, 8, 10, 12, 15]
def divby3(i):
    return i%3==0
print(list(filter(divby3,[3, 6, 8, 10, 12, 15])))

x=lambda i:i%3==0
print(list(filter(x,[3, 6, 8, 10, 12, 15])))


#11.Keep words longer than 4 letters
words = ["cat", "elephant", "dog", "tiger"]
def long(i):
    return len(i)>4
print(list(filter(long,["cat", "elephant", "dog", "tiger"])))

x=lambda i:len(i)>4
print(list(filter(x,["cat", "elephant", "dog", "tiger"])))

#12.Keep palindromes
words = ["madam", "python", "level", "world"]
def long(i):
    return i==i[::-1]
print(list(filter(long,["madam", "python", "level", "world"])))

x=lambda i:i==i[::-1]
print(list(filter(x,["madam", "python", "level", "world"])))

#13.Keep uppercase words
words = ["HELLO", "world", "PYTHON", "code"]

def long(i):
    return i.isupper()
print(list(filter(long,["HELLO", "world", "PYTHON", "code"])))

x=lambda i:i.isupper()
print(list(filter(x,["HELLO", "world", "PYTHON", "code"])))

#14.Filter names that end with “n”
names = ["Arun", "Kiran", "Deepak", "Sohan"]
def long(i):
    return i.endswith('n')
print(list(filter(long,["Arun", "Kiran", "Deepak", "Sohan"])))

x=lambda i:i.endswith('n')
print(list(filter(x,["Arun", "Kiran", "Deepak", "Sohan"])))

#15.Keep numbers within a range (10–20)
nums = [5, 10, 15, 20, 25]
def long(i):
    return 10<=i<=20
print(list(filter(long,[5, 10, 15, 20, 25])))

x=lambda i:10<=i<=20
print(list(filter(x,[5, 10, 15, 20, 25])))

#16.Filter emails containing “@gmail.com”
emails = ["mailto:abc@gmail.com", "mailto:xyz@yahoo.com", "mailto:test@gmail.com"]

def mail(i):
    return i.endswith("@gmail.com")
print(list(filter(mail,["mailto:abc@gmail.com", "mailto:xyz@yahoo.com", "mailto:test@gmail.com"])))

x=lambda i:i.endswith("@gmail.com")
print(list(filter(x,["mailto:abc@gmail.com", "mailto:xyz@yahoo.com", "mailto:test@gmail.com"])))

#17.Keep tuples where sum > 10
pairs = [(1,2), (5,6), (3,4), (7,8)]
def tu(i):
    return sum(i)>10
print(list(filter(tu,[(1,2), (5,6), (3,4), (7,8)])))

x=lambda i:sum(i)
print(list(filter(x,[(1,2), (5,6), (3,4), (7,8)])))



#18.wap to return a list having only flowers
l=["sun flowers","banana tree","lily flowers","lotus flower","marigold flowers"]
def flower(i):
    return i.endswith("flowers")
print(list(filter(flower,["sun flowers","banana tree","lily flowers","lotus flower","marigold flowers"])))

x=lambda i: i.endswith("flowers")
print(list(filter(x,["sun flowers","banana tree","lily flowers","lotus flower","marigold flowers"])))
"""