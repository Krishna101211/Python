''''
# 16.wap to create a dictionary words and its length pair
s = "tomorrow is weekend and non-veg special"
# o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}
d={}
for i in s.split(" "):
     d[i]=[len(i)]
print(d)

# 17.wap to create a dictionary characters and its corresponding upper case characters
s = "sunday"
# o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}
d={}
for i in s:
     i.split()
     d[i]=i.upper()
print(d)


# 18.wap to create a dictionary Ascii and character pair
l = [89, 51, 111, 77, 108, 120]
# o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}
d={}
for i in l:
     d[i]=chr(i)
print(d)


# 19.wap to  create a list of characters and its Ascii value pair
s = "sunday"
# o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)]
l=[]
for i in s:
     i.split()
     l.append((i,ord(i)))
print(l)


# 20.wap to create a dictionary with words and ??????????
# its length pair and ends with vowel
s = "Anna is here to enjoy a banana"
# o/p{'Anna': 4, 'to': 2, 'enjoy': 5, 'a': 1, 'banana': 6}



# 21.wap to create a dictionary with letter and its words starting with that letter pair ?????????
s = "hi hello good morning welcome to python session"
# o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'], 't': ['to'], 'p': ['python'], 's': ['session']}


# 22.wap to create a dictionary of characters and its indices pair ????
s = "hello python"
# o/p:-->{"h":[0,9],"e":1..........}


# 23.wap to create a dictionary word and reverse word pair
s = "tomorrow is weekend and non-veg special"
# o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and': 'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}
d={}
for i in s.split(" "):
     d[i]=[i[::-1]]
print(d)
'''
# 24.Reverse a list without using any built-in functions and slicing.
l = [1, 2, 3, 4]

# 25.wap to Sum of numbers
s = 'Sony12India567pvt21ltd'

# 26.Print all the missing numbers from 1-10 in the below list
l = [1, 2, 3, 4, 6, 7, 10]

# 27.WAP to remove duplicates from the list without using inbuilt function
d = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4]

# 28.wap to replace all the character with "-" if the characters occurs more than once in a string
s = "hellohai"
# o/p---->-e--o-ai


# 29.wap to print first and last char of each name in the list
a = ["Sunil", "anil", "Suresh", "Mahesh", "Dinesh"]

# 30.wap to create a new list as square of each number of below list
b = [2, 4, 5, 6, 7, 1]

# 31.wap if number is even the print its square else print its cube
c = [2, 4, 5, 3, 7, 9]

# 32.wap to create a list with square and cube of each numbers
d = [2, 4, 5, 1, 8, 9, 10]
# o/p-->[(4, 8), (16, 64), (25, 125), (1, 1), (64, 512), (81, 729), (100, 1000)]


# 33.wap to create a new list of reversing each name from the list
names = ["prince", "Rekha", "Madhu", "Sindhu", "denga", "manga"]

# 34.wap to create a new list, of individual and collection data type from list
data = [20.12, True, [10, 20], "super", {1, 2}, {"a": 10}, 100, (8, 9)]

# 35.wap to create a dictionary characters and its count pair
char = ["a", "M", "i", "A", "M", "I", "i", "H", "a", "H"]

# 36.wap to group fruit name and country pair
d = {"apple": 45, "mango": 67, "cherry": 90, "berry": 23}
p = {"Kashmir": "India", "America": "us", "UK": "Toronto", "Africa": "Uganda"}

# 37.wap to sum of same index element from l1,l2,l3
l1 = [10, 20, 30, 40]
l2 = [78, 44, 11, 99]
l3 = [1, 2, 3, 4]

# 38.wap to pair values of both dictionary
d = {"apple": 45, "mango": 67, "cherry": 90, "berry": 23}
p = {"Kashmir": "india", "America": "us", "UK": "Toronto", "Africa": "Uganda"}

# 39. WAP to extract only file names
l = ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx',
     'lambda.png', 'map.py', 'python.pdf', 'oops.py']
# output:-['forloop', 'python', 'while', 'functions', 'lambda', 'map', 'oops']


# 40WAP to get the given o/p
s = 'hi hello good morning'
# exp o/p: 'gninrom doog olleh ih'


# 41.wap to print a-z character

# 42.wap to print a-z character