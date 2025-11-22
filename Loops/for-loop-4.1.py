# 16.wap to create a dictionary words and its length pair
# s = "tomorrow is weekend and non-veg special"
# o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}
# d={}
# for i in s.split(" "):
#      d[i]=[len(i)]
# print(d)


# 17.wap to create a dictionary characters and its corresponding upper case characters
# s = "sunday"
# o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}
# d={}
# for i in s:
#      i.split()
#      d[i]=i.upper()
# print(d)


# 18.wap to create a dictionary Ascii and character pair
# l = [89, 51, 111, 77, 108, 120]
# o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}
# d={}
# for i in l:
#      d[i]=chr(i)
# print(d)


# 19.wap to  create a list of characters and its Ascii value pair
# s = "sunday"
# o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)]
# l=[]
# for i in s:
#      i.split()
#      l.append((i,ord(i)))
# print(l)


# 20.wap to create a dictionary with words and its length pair and ends with vowel
# s = "Anna is here to enjoy a banana"
# o/p{'Anna': 4, 'to': 2, 'enjoy': 5, 'a': 1, 'banana': 6}
# d={}
# v="AEIOUaeiou"
# for i in s.split():
#    if i[-1] in v :
#      d[i]=len(i)
# print(d)


# 21.wap to create a dictionary with letter and its words starting with that letter pair
# s = "hi hello good morning welcome to python session"
# o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'], 't': ['to'], 'p': ['python'], 's': ['session']}
# d={}
# for w in s.split():
#     key = w[0]     # first letter of word
#     if key not in d:
#         d[key] = []     # create empty list
#     d[key].append(w)    # add word to list
# print(d)


# 22.wap to create a dictionary of characters and its indices pair
# s = "hello python"
# o/p:-->{"h":[0,9],"e":1..........}
# d = {}   # empty dictionary
# for i in range(len(s)):
#     ch = s[i]
#     if ch != " ":        # ignore spaces
#         if ch not in d:
#             d[ch] = []   # create empty list
#         d[ch].append(i)  # add index to list
# print(d)


# 23.wap to create a dictionary word and reverse word pair
# s = "tomorrow is weekend and non-veg special"
# o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and': 'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}
# d={}
# for i in s.split(" "):
#      d[i]=[i[::-1]]
# print(d)


# 24.Reverse a list without using any built-in functions and slicing.
# l = [1, 2, 3, 4]
# reverse=[]
# for i in l:
#      reverse=[i]+reverse
# print(reverse)


# 25.wap to Sum of numbers
# s = 'Sony12India567pvt21ltd'
# sum=0
# for i in s:
#      if i.isdigit():
#           sum=sum+int(i)
# print(sum)

#If your goal is to sum full numbers (12 + 567 + 21)
# s = 'Sony12India567pvt21ltd'
# sum_num = 0
# temp = ""
# for ch in s:
#     if ch.isdigit():
#         temp += ch      # build the number
#     else:
#         if temp != "":
#             sum_num += int(temp)
#             temp = ""   # reset number
# # Add the last number if present
# if temp != "":
#     sum_num += int(temp)
# print(sum_num)


# 26.Print all the missing numbers from 1-10 in the below list
# l = [1, 2, 3, 4, 6, 7, 10]
# for i in range(1, 11):     # from 1 to 10
#     if i not in l:
#         print(i)


# 27.WAP to remove duplicates from the list without using inbuilt function
# d = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4]
# k=[]
# for i in d:
#      if i not in k:
#           k.append(i)
# print(k)


# 28.wap to replace all the character with "-" if the characters occurs more than once in a string
# s = "hellohai"
# o/p---->-e--o-ai
# o=''
# for ch in s:
#     if s.count(ch) > 1:      # occurs more than once
#         o += "-"             # replace with -
#     else:
#         o += ch              # keep the character
# print(o)


# 29.wap to print first and last char of each name in the list
# a = ["Sunil", "anil", "Suresh", "Mahesh", "Dinesh"]
# k=[]
# for i in a:
#      k.append((i[0],i[-1]))
# print(k)

# 30.wap to create a new list as square of each number of below list
# b = [2, 4, 5, 6, 7, 1]
# s=[]
# for i in b:
#      s.append(i*2)
# print(s)

# 31.wap if number is even the print its square else print its cube
# c = [2, 4, 5, 3, 7, 9]
# s=[]
# for i in c:
#      if i%2==0:
#           s.append(i*2)
#      else:
#           s.append(i**3)
# print(s)


# 32.wap to create a list with square and cube of each numbers
# d = [2, 4, 5, 1, 8, 9, 10]
# o/p-->[(4, 8), (16, 64), (25, 125), (1, 1), (64, 512), (81, 729), (100, 1000)]
# s=[]
# for i in d:
#           s.append((i*2,i**3))
# print(s)

# 33.wap to create a new list of reversing each name from the list
# names = ["prince", "Rekha", "Madhu", "Sindhu", "denga", "manga"]
# new_list = []
# for name in names:
#     new_list.append(name[::-1])
#
# print(new_list)

# 34.wap to create a new list, of individual and collection data type from list
# data = [20.12, True, [10, 20], "super", {1, 2}, {"a": 10}, 100, (8, 9)]
# individual = []
# collection = []
# for item in data:
#     if type(item) in (list, tuple, set, dict):
#         collection.append(item)
#     else:
#         individual.append(item)
# print("Individual:", individual)
# print("Collection:", collection)


# 35.wap to create a dictionary characters and its count pair
# char = ["a", "M", "i", "A", "M", "I", "i", "H", "a", "H"]
# d = {}
# for c in char:
#     d[c] = d.get(c, 0) + 1
#
# print(d)


# 36.wap to group fruit name and country pair
# d = {"apple": 45, "mango": 67, "cherry": 90, "berry": 23}
# p = {"Kashmir": "India", "America": "us", "UK": "Toronto", "Africa": "Uganda"}
# result = {}
# for (fruit, num), (place, country) in zip(d.items(), p.items()):
#     result[fruit] = (place, country)
#
# print(result)


# 37.wap to sum of same index element from l1,l2,l3
# l1 = [10, 20, 30, 40]
# l2 = [78, 44, 11, 99]
# l3 = [1, 2, 3, 4]
# result = []
# for i in range(len(l1)):
#     result.append(l1[i] + l2[i] + l3[i])
#
# print(result)


# 38.wap to pair values of both dictionary
# d = {"apple": 45, "mango": 67, "cherry": 90, "berry": 23}
# p = {"Kashmir": "india", "America": "us", "UK": "Toronto", "Africa": "Uganda"}
# pair = {}
# for (k1, v1), (k2, v2) in zip(d.items(), p.items()):
#     pair[k1] = v1
#     pair[k2] = v2
# print(pair)


# 39. WAP to extract only file names
# l = ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx',
#      'lambda.png', 'map.py', 'python.pdf', 'oops.py']
# output:-['forloop', 'python', 'while', 'functions', 'lambda', 'map', 'oops']
# names = []
# for file in l:
#     names.append(file.split('.')[0])
# print(names)


# 40WAP to get the given o/p
# s = 'hi hello good morning'
# exp o/p: 'gninrom doog olleh ih'
# words = s.split()
# rev = ""
# for w in words[::-1]:
#     rev += w[::-1] + " "
# print(rev.strip())


# 41.wap to print a-z character
# for i in range(97, 123):
#     print(chr(i), end=" ")


# 42.wap to print a-z character
# for i in range(65, 91):
#     print(chr(i), end=" ")
