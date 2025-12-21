# . Matches any number between 0-9
import re
# a="The cost of the book is Rs.100"
# print(re.findall(r'[0-9]',a))

# 2. Matches only lower case and upper case letters
# b="hello HOW ARE YOU"
# print(re.findall(r'[a-zA-Z]',b))

# 3. Count the number of white spaces
# c="HELLO world welcome to python Hi how are you. Hi how are you"
# print(len(re.findall(r'\s',c)))

# 4. Sum all the numbers in the string
# word="PYTHON12nREG567exp2"
# print(sum(map(int,re.findall(r'\d+',word))))

# 5. Matches everything apart from numbers 0-9
# a="The cost of the book is Rs.100"
# print(re.findall(r'[^0-9]',a))

# 6. Matches everything apart from "a","b","c","d"
# b="abcdefghijklmnop"
# print(re.findall(r'[^abcd]',b))

# 7. Matches only numbers
# word="@hello12world34welcome!123"
# print(re.findall(r'\d+',word))

# 8. Extracting file with extension
# s="Downloading archive.zip file to download folder python hero.py and afternoon.txt and slicing.jpeg"
# print(re.findall(r'\w+\.\w+',s))

