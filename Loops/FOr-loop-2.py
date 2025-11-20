
'''
#
# 3.wap to capitalize only the first letter of every word in
# the given list
# l=["vaidegi","rahul","shivam","kapil","patil"]
# for i in l:
#     print(i.capitalize())


# 4.wap to extract only individual data types form the list
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# for i in l:
#     if type(i) in (int,float,complex,bool):
#         print(i)
# print()
# for i in l:
#     if isinstance(i,(int,float,complex,bool)):
#         print(i)

# 5.wap to extract only individual data types from the list and
# sum all the individual data types
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# Total=0
# for i in l:
#     if isinstance(i,(int,float,complex,bool)):
#         print(i)
#         Total=Total+i
# print(Total)
""" 
step-->1 
Total=0 
for "hello" in l: 
    if isinstance('hello',(int,float,complex,bool)):False 

step-->2 
Total=0 
for 1 in l: 
    if isinstance(1,(int,float,complex,bool)):True 
        Total=Total+1---->Total=1 


step-->3 
Total=1 
for 23.4 in l: 
    if isinstance(23.4,(int,float,complex,bool)):True 
        Total=Total+23.4---->Total=24.4 

step-->4 
Total=1 
for 5+6j in l: 
    if isinstance(5+6j,(int,float,complex,bool)):True 
        Total=Total+5+6j---->Total=29.4+6j 

#Total=29.4+6j+True---->30.4+6j     
"""
# 6.wap to print the count of alphabets and numbers
# and space in the given string
# s="india got the independence in the year 1947"
# alphabet=0
# number=0
# space=0
# for i in s:
#     if i.isalpha():
#         alphabet=alphabet+1
#     elif i.isdigit():
#         number=number+1
#     else:
#         space+=1
# print(alphabet)
# print(number)
# print(space)

# 7.wap to check how many words are present in the given sentence
s = "hello world sentence"
total_word = 0
for i in s.split():
    total_word = total_word + 1
print(total_word)

# 8.wap to create a dictionary and print the characters
# and its Ascii value pair
s = "hello world"
# output:--> {"h":ascii value,"e":ascii value........}

# 9.wap to create a dictionary and traverse into
# it and if the length is even print as it else reverse it
names = ["apple", "google", "yahoo", "microsoft", "gmail", "walmart"]
# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}
d = {}
for i in names:
    if len(i) % 2 == 0:
        d.update({i: i})  # d[i]=i
    else:
        d.update({i: i[::-1]})  # d[i]=i[::-1]
print(d)

# 10.wap to print series of factorial(take user input)

# 11.wap to create a dictionary with element and its count pair
l = ["yellow", "red", "black", "pink", "orange", "green", "red", "pink", "yellow"]
# output:-->
# {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}

e = {}
for i in l:
    e.update({i: l.count(i)})  # e[i]=l.count(i)
print(e)

# 12.wap to find the length of the string without using inbuilt function
s = "Never Give Up"
length = 0
for i in s:
    length = length + 1
print(length)

# 13.wap to reverse a string without using inbuilt function
x = "you did it guys"
res = ''
for i in x:
    res = i + res
print(res)
'''