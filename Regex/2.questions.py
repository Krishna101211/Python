# . Matches any number between 0-9
import re
# a="The cost of the book is Rs.100"
# print(re.findall(r'[0-9]',a))
#
# 2. Matches only lower case and upper case letters
# b="hello HOW ARE YOU"
# print(re.findall(r'[a-zA-Z]',b))
#
# 3. Count the number of white spaces
# c="HELLO world welcome to python Hi how are you. Hi how are you"
# print(len(re.findall(r'\s',c)))
#
# 4. Sum all the numbers in the string
# word="PYTHON12nREG567exp2"
# print(sum(map(int,re.findall(r'\d+',word))))
#
# 5. Matches everything apart from numbers 0-9
# a="The cost of the book is Rs.100"
# print(re.findall(r'[^0-9]',a))
#
# 6. Matches everything apart from "a","b","c","d"
# b="abcdefghijklmnop"
# print(re.findall(r'[^abcd]',b))
#
# 7. Matches only numbers
# word="@hello12world34welcome!123"
# print(re.findall(r'\d+',word))
#
# 8. Extracting file with extension
# s="Downloading archive.zip file to download folder python hero.py and afternoon.txt and slicing.jpeg"
# print(re.findall(r'\w+\.\w+',s))
#
# 9. Extract only pincode
# s="Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"
# print(re.findall(r'\b\d{6}\b',s))
#
# 10. Print the AADHAR CARD numbers
# s="my aadhar number is 1234-4567-8910"
# print(re.findall(r'\d{4}-\d{4}-\d{4}',s))
#
# print(re.findall(r'[0-9]+',s))
#
# print(re.findall(r'[\b\d]+',s))

# 11. Print the PAN card numbers
# a="my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"
# print(re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]',a))

# 12. Fetch the protocols
# a="https://www.google.com"
# print(re.findall(r'[a-zA-Z0-9]+',a))          # ['https','www','google','com']
# print(re.findall(r'https?://[^\s]+',a))       # ['https://www.google.com']
#
# 13. Creating acronyms
# file_format=["Graphic Interchange Format","Advanced Audio Coding",
#              "HyperText Markup Language","Content Management System",
#              "Windows Media,Audio","Comma Separated Values"]
#
# print([''.join(re.findall(r'\b[A-Z]',i)) for i in file_format])

# 14. Match valid email IDs
emails=["test.user@company.gov","test_user@company.edu",
        "123test-T.user@company.in","testing@company","pspider@company.in"]

# print([i for i in emails if re.findall(r'[A-Za-z0-9._]+@[a-z0-9.-]+\.[a-z]{2,}',i)])
print([i for i in emails if re.findall(r'@company',i)])

# 15. Match valid phone numbers (xxx-xxx-xxxx)
phonenumbers=["123-345-0987","456-9832-098","800-987-4756",
              "080-1029384727","123-345-12","900-938-0987"]
print([i for i in phonenumbers if re.fullmatch(r'\d{3}-\d{3}-\d{4}',i)])

# 16. Replace whitespace with newline
s="helloworld welcome to python"
print(re.sub(r'\s','\n',s))
print(re.sub(r'\W','\n',s))

# 17. Replace all digits with **
s="hello 123 mic testing 123 123"
print(re.sub(r'\d+','**',s))
print(re.sub(r'[0-9]+','**',s))










# 18. Extract dates
# date="The event is scheduled for 22-05-2025 or 22/05/2025."
# print(re.findall(r'\b\d{2}[-/]\d{2}[-/]\d{4}\b',date))
