# FOR LOOP  level one questions

# 1.wap to print the number form 1 -20 segregate even and
# odd number into list
# e=[]
# o=[]
# for i in range(0,21,1):
#     if i%2==0:
#         e.append(i)
#     else:
#         o.append(i)
# print(e)
# print(o)


# 2.wap to extract vowels and digits in a string { how to add digits ?}
# s = "hello123"
# v='aeiou'
# v_1=""
# digit=""
# for i in s:
#     if i in v:
#         v_1=v_1+i
#     elif i.isdigit():
#         digit=digit+i
# print(digit)
# print(v_1)


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
from operator import index

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
# s="hello world sentence"
# total_word=0
# for i in s.split():
#     total_word=total_word+1
# print(total_word)

# 8.wap to create a dictionary and print the characters
# and its Ascii value pair
# output:--> {"h":ascii value,"e":ascii value........}
# s = "hello world"
# d = {}
# for char in s:
#     d[char] = ord(char)  # map character to ASCII value
# print(d)

# 9.wap to create a dictionary and traverse into
# it and if the length is even print as it else reverse it
# names = ["apple", "google", "yahoo", "microsoft", "gmail", "walmart"]
# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}
# d={}
# for i in names:
#     if len(i)%2==0:
#         d.update({i:i})   #d[i]=i
#     else:
#         d.update({i:i[::-1]})  #d[i]=i[::-1]
# print(d)


# 10.wap to print series of factorial(take user input)
# fact=1
# num=int(input("enter the number:--->"))
# for i in range (1,num+1):
#     print(i)
#     fact=fact*i
# print(fact)


# 11.wap to create a dictionary with element and its count pair
# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# # output:-->
# # {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}
# e={}
# for i in l:
#     e.update({i:l.count(i)})  #e[i]=l.count(i)
# print(e)


# 12.wap to find the length of the string without using inbuilt function
# s="Never Give Up"
# length=0
# for i in s:
#     length=length+1
# print(length)


# 13.wap to reverse a string without using inbuilt function
# x="you did it guys"
# res=''
# for i in x:
#     res=i+res
# print(res)


# 14.wap to print alternative character from a given string
# s = "hello python"
# for i in range(0,len(s),2):
#     print(s[i])


# 15.wap to create a dictionary index and word pair
s = "tomorrow is weekend and non-veg special"
# o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}
d={}
words=s.split()
for i in range(len(words)):
    d[i]=words[i]
print(d)