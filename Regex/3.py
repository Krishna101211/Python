import re

# wap to match email id's
emails = [
    "mailto:user.name123@gmail.com",
    "mailto:username@yahoo.in",
    "mailto:test.email+alex@outlook.com",
]

# matching phone numbers(in us style-->(3,3,4)
phonenumbers = ["123-345-0987", "456-9832-098", "800-987-4756",
                "080-1029384727", "123-345-12", "900-938-0987"]

# .wap to extract only pincode
s = ("Bangalore pincode is 560001 and area code is BSK234567 and "
     "state code is KAR123")

# .wap to print the AADHAR CARD numbers
x = "my aadhar number is 1234-4567-8910"

# .wap to print the pan card number
a = ("my pan number is ABCDE1234X and other number is PQRST5678W "
     "and id is 123abcd45")

# .How to fetch the protocols
b = "https://www.google.com"
# o/p:-o/p--->['https', 'www', 'google', 'com'] (i want first output like this )
# o/p--->['https://www.google.com']        (second output)


# .creating acronyms of the file format
file_format = ["Graphic Interchange Format",
               "Advanced Audio Coding",
               "HyperText Markup Language",
               "Content Management System",
               "Windows Media,Audio",
               "Comma Separated Values"]
# o/p--> GIF,AAC,HTML,CMS,WMA,CSV
for i in file_format:
    pattern = re.findall('[A-Z]', i)
    print("".join(pattern))

# replace whitespace with newline characters
w = "helloworld welcome to python"

# replace all digits with **
q = "hello 123 mic testing 123 123"

# print onlt date of birth
text = "My date of birth is 22-05-2025"
"""
            interview questions

1.What is a Regular Expression (Regex)?
→ Explain definition, usage in pattern matching, validation, and searching.

2.What’s the difference between match(), 
search(), and findall() in Python regex?

match() → checks only at the beginning.
search() → checks the whole string for the first occurrence.
findall() → returns all matches as a list.


3.What is the difference between \d, \w, and \s?

\d → digits (0–9)

\w → word characters (a-zA-Z0-9_)

\s → whitespace (space, tab, newline)


4.Explain the difference between . (dot) and * (asterisk) in regex.

. → matches any single character except newline.
* → quantifier meaning 0 or more occurrences.

5.What is the role of ^ and $ in regex?

^ → beginning of the string.
$ → end of the string.

6.What is the difference between group() and groups()?

group() → returns the entire match or a specific group.
groups() → returns all captured groups as a tuple.
"""
