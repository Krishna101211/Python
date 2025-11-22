""" list comprehension syntax syntax-->1 without if-else block var_name=[operation(inseration /update/print) forloop condition]
 syntax--->2 with simple if condition var_name=[TSB forloop condition if condition]
 syntax--->3 with both if-else block var_name=[TSB if condition else block for loop condition]


--------------------------------------------------------------------------
 set comprehension syntax syntax-->1 without if-else block var_name={operation(inseration/update/print) forloop condition}
 syntax--->2 with simple if condition var_name={TSB forloop condition if condition}
 syntax--->3 with both if-else block var_name={TSB if condition else block for loop condition}


 --------------------------------------------------------------------------
 Dict comprehension syntax syntax-->1 without if-else block var_name={Key:Value forloop condition}
 syntax--->2 with simple if condition var_name={key:value(TSB) forloop condition if condition}
  syntax--->3 with both if-else block var_name={Key:value(TSB) if condition else block for loop condition} """
from os.path import split
from xmlrpc.client import boolean


""" #nested comprehension syntax without if-else condition var_name=[operation outer for loop inner for loop] 
with simple if condition var_name=[operation outer for loop inner for loop if condition] 
with both if-else block var_name=[TSB if condition else block outer for loop inner for loop] """



""" 
list comprehension example 
1. Squares of numbers divisible by 3 (1–30) 2. Cube of odd numbers (1–20)
x=[i**2 if i%2==0 else i**3 for i in range(1,31)]
#3. Words with length > 4
words = ["apple", "bat", "banana", "cat", "elephant"]
h=[i for i in words if len(i)>4 ]

#4. Remove vowels from a string
text = "list comprehension"
x=[i for i in text if i not in "aeiouAEIOU" ]

#5. Extract only integers from a mixed list
items = [1, "apple", 2.5, 3, "banana", 4]
x=[i for i in items if isinstance(i,int)]
print(x)
#6. Reverse words containing the letter ‘a’
words = ["cat", "dog", "apple", "ball"]
x=[i[::-1]  if 'a' in i or 'A' in i else i for i in words]
print(x)

#7. Words converted to title case words = ["python", "java", "machine learning"]
#8.Numbers divisible by 4 but not by 8 (1,51)
x=[i for i in range(1,52) if i%4==0 and i%8!=0]
print(x)

#9.List of ASCII values of characters chars = ['A', 'B', 'C', 'a', 'b']
#10.Characters from string at even indexes
text = "comprehension"
x = [ch for idx, ch in enumerate(text) if idx % 2 == 0]
#11.Words starting and ending with same letter
words = ["level", "radar", "apple", "deed"]
z=[i  for i in words if i[::]==i[::-1]]
print(z)
#12.First letter of each word words = ["apple", "banana", "cherry"]
#13.Convert list of strings to uppercase
fruits = ["apple", "banana", "cherry"]
l=[i.upper() for i in fruits]
print(l)


#14.Extract uppercase letters from a string
text = "PyThOn LiSt Comprehension"
x=[i for i in text if i.isupper()]
print(x)
"""


#15.Extract first names from full names
names = ["John Smith", "Alice Brown", "Mark Lee"]
x = [i.split()[0] for i in names]
print(x)


#import numpy as np  Dictionary comprehension example
# 1.number and its square (1–10)------>x={i:i**2 for i in range(1,11)}
# 2.Number and its cube (1–5)---------->x={i:i**3 for i in range(1,6)}
# 3.Character and ASCII value---->#y="Master mind"------->x={i:ord(i) for i in y}
#4. Word and its length words------>y=["apple", "banana", "cherry"]------>x={i:len(i) for i in y}
#5. string to reversed string words--->k= ["hello", "world", "python"]----->x=[i[::-1] for i in k ]
#6.#wap to create a dictionary +ve number as key and convert to -ve number # as a value------->x=[-8,6,8,-5,9,8,4,-67]------>y = {i: -i for i in x if i > 0}
# 7.wap to create a dictionary element and its data type pair only element should be individual data type----->l=[10,"hai",9.3,4+4j,(11,22),{2,3},False,[1,3]]----->k={i:type(i) for i in l if isinstance(i,(int,complex,bool,float)) }
# 8.wap to create a dictionary convert uppercase to lowercase and lowercase to uppercase-----> s="FrIdAy"----->l={i:i.lower() if i.isupper() else i.upper() for i in s}
# 9.wap to create a dictionary characters and its count pair------->char=["a","M","i","A","M","I","i","H","a","H"]------->o={i:char.count(i) for i in char }
# 10..wap to create a dictionary with words and its length pair and ends with vowel
# #o/p{'Anna': 4, 'to': 2, 'enjoy': 5, 'a': 1, 'banana': 6} """----->s = "Anna is here to enjoy a banana"----->y={i:len(i) for i in s.split() }