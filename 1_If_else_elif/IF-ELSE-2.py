'''
#1
x=int(input())
if x>0 :
    print("Number is +ve")
else:
    print("Number is -ve")

#2
x=eval(input())
if x%2==0 :
    print("Number is even")
else:
    print("Number is odd")

#3
x=eval(input())
if x>10 :
    print("Number is greater than 10")
else:
    print("Number is not greater than 10")

#4
x=eval(input())
if x%3==0 and x%5==0:
    print("GOOD MORNING")
else:
    print("GOOD EVENING")

#5
x=eval(input())
y=eval(input())
if x==y:
    z=x*y
    print(z)
else:
    c=x**y
    print(c)

#6
x=eval(input())
y=eval(input())
if x>y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is greater than {x}")

#10
x=eval(input())
if x%2==0:
    y=x+1
    print(f"{y}Number is odd")
else:
    z=x+1
    print(z)

#11
x=eval(input())
if x%3==0:
    print(f"{x} is divisible by 3")
else:
    z=x**3
    print(f"{z} it is cube of {x}")

#12
x=eval(input())
if x%3==0 and x%5==0:
    print(f"{x} is divisible by 3")
else:
    print({str(x)})

#13
x=eval(input())
if 1<=x<=19:
    y=x**2
    print((y))
else:
    z=x**3
    print((z))

#14
score=eval(input())
if score>40:
    print(f" Student is passed {score}")
else:
    print(f" Student is failed {score}")

#15
x=eval(input())
if 47<=x<=58 and x%2==0:
    print(f"{ord(x)} it is ascii of {x}")
else:
    y=x//5
    print(f"{y}  floor division value ")

#16
d={}
l=[]
x=eval(input())
if 47<=x<125:
    d.update({f"{x}":f"{x}"})
    print(f"{d} it is ascii of ")
else:
    l.append(x)
    print(f"{l} list value ")
'''
#--------------2 page -------------------------------------------------
'''
 #17
x=str(input())#why eval didnt work 
if x.isalpha():
    print(f"{x}only charter is present")
else:
    print(f"{x} not alphabet ")

#18
x=str(input())#why eval didnt work 
if x.isupper():
    print(f"{x}only charter is present is upper")
else:
    print(f"{x} not upper ")

#19
x=str(input())#why eval didnt work 
if x.islower():
    print(f"{x}only charter is present is lower")
else:
    print(f"{x} not all lower ")

#20
x=str(input())#why eval didnt work 
if x.isupper():
    y=x.lower
    print(f"{y}only charter is present is upper")
else:
    print(f"{ord(x)} not upper ")

#21
x=str(input())#why eval didnt work 
if x.islower():
    y=x.upper()
    print(f"{y}only charter is present is upper")
else:
    z=x.lower()
    print(f"{(z)} not upper ")

#22------------------------------------?????
x=str(input())
if 9<=ord(x[0])<=122:
    y=len(x)%2
    z=x[y]
    print(z)
else:
    k=x[-1::]
    y = len(k) % 2
    print(y)

#23
d="aeiou"
x=str(input())
if x in d:
    print(f"{x} is voewl ")
else:
    print("x is ‘CONSONANT ")

#24????????
# Program to check whether a character is a vowel or consonant
# and print next or previous character accordingly

# Get input from the user
ch = input("Enter a single alphabet character: ")

# Check if input is a single alphabet character
if len(ch) == 1 and ch.isalpha():
    # Convert to lowercase for uniform comparison
    ch_lower = ch.lower()
    
    # Check if it's a vowel
    if ch_lower in ['a', 'e', 'i', 'o', 'u']:
        # Print next character
        next_char = chr(ord(ch) + 1)
        print(f"'{ch}' is a vowel. Next character is '{next_char}'")
    else:
        # Print previous character
        prev_char = chr(ord(ch) - 1)
        print(f"'{ch}' is a consonant. Previous character is '{prev_char}'")
else:
    print("Invalid input. Please enter a single alphabet letter.")


#25??????????????????????
x=str(input())
if 9<=ord(x[0])<=122:
    k = x[-1::-1]
    print(x,k)
else:
    y = len(x) % 2
    print(x[y])

#26
x=str(input())
if len(x)<3:
    print(x)
else:
    print(x[3:len(x)])

#27
x=str(input())
if len(x)%2==0:
    print(x+'bye')
else:
    print(x[0],x[-1])

#28????????????
x=str(input())
if len(x)%2==1:
    print('haii'+x)
else:
    print(x[1:-2:-1])#??????
    
#29????????????
#---------------page 3------------------------------------------------------
#30 WAP to check whether a given year is a leap year or not. if leap year, print leap 
#year or else not a leap year.
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#40 WAP to find out the greatest of two numbers and display the greatest number. 
#if the greatest number, display the greatest message with value. 
a = 15
b = 10
if a > b:
    print("Greatest number:", a)
else:
    print("Greatest number:", b)

#41 WAP to check whether the given value is present inside the given collection or 
#not.if value is present, display the value is available or else the value is not present. 
val = 5
coll = [1, 3, 5, 7]
if val in coll:
    print("Value is available")
else:
    print("Value is not present")

#42 String First and Last Character Switch or Repeat ?????
s = "hello"
if len(s) > 2:
    new_s = s[-1] + s[1:-1] + s[0] #s[1:-1] will use to print string without 1st and last postion 
    print(new_s)
else:
    print(s * 3)

#43 List Check and Modify ??????
val = [9, 'abc', 6]
if type(val) == list and isinstance(val[0], int) and isinstance(val[-1], int):
    if val[0] % 3 == 0:
        val[0] = True
    val[-1] = ~val[-1]
    print(val)
else:
    print(len(val) ** 2)

#44 String Check and Insert or Repeat ???????
val = "abcdefgh"
if type(val) == str and len(val) > 7:
    middle = len(val) // 2
    val = val[:middle] + "NEW" + val[middle:]
    print(val)
else:
    print(val * 3)

#45 First Two Characters Sequence or Reverse Half
s = "abcdef"
if ord(s[1]) - ord(s[0]) == 1:
    print(s[0] + s[1] + s[-2:])
else:
    mid = len(s) // 2
    print(s[:mid][::-1] + s[mid:])

#46 Value Present in Collection
val = 3
coll = [1, 2, 3, 4]
if val in coll:
    print("Value:", val)
else:
    print("Value not found")

#47 Key Check in Dictionary
d = {"a": 1, "b": 2}
key = "c"
if key in d:
    print("Value:", d[key])
else:
    d[key] = 99
    print("Updated dict:", d)

#48 Check Set and Append or Remove Duplicates
coll = {1, 2, 3}
if type(coll) == set:
    coll.add(4)
    print(coll)
else:
    coll = set(coll)
    print(coll)

#49 Age Eligibility for Vote
age = 20
if age >= 18:
    print("Age:", age, "Eligible to vote")
else:
    print("Not eligible")

#50 Even Check and ASCII or Floor Division??????
val = 48
if val % 2 == 0 and 47 < val < 58 and val != 0:
    print("ASCII:", chr(val))
else:
    print(val // 5)
#---------------page 4-----------------------------------------------------------
#51  Palindrome String Check
s = "madam"
if s == s[::-1]:
    print("Palindrome:", s)
else:
    print("Not palindrome")

#52  Palindrome Number Check
num = 121
if str(num) == str(num)[::-1]:
    print("Palindrome:", num)
else:
    print("Not palindrome")

#53 Length of Both Strings Equal or Not
s1 = "abc"
s2 = "xyz"
if len(s1) == len(s2):
    print(s1 + s2)
else:
    print(s1, len(s1), s2, len(s2))

#54 Same Memory Location Check
a = [1, 2, 3]
b = a
if a is b:
    print("Middle of b:", b[len(b)//2])
else:
    print("First & Last of a:", a[0], a[-1], id(a))

#55 String ASCII + Div by 5 or Repeat??????????????????????
s = "abcdefghijk"
if len(s) > 10 and (ord(s[0]) + ord(s[-1])) % 5 == 0:
    print("ASCII:", ord(s[0]), ord(s[len(s)//2]), ord(s[-1]))
else:
    print(s * 3)

#56 Middle Item String Check in List
lst = [1, "hello", 3]
mid = len(lst) // 2
if isinstance(lst[mid], str):
    print(lst)
else:
    print(lst[mid])

#57 Exchange First and Last Character?????????
s = "python"
if len(s) > 1:
    print(s[-1] + s[1:-1] + s[0])
else:
    print(s)

#58 Divisible by 7 but Not 5
num = 49
if num % 7 == 0 and num % 5 != 0:
    print("Valid:", num)
else:
    print(num * 4)

#59 Same Memory Address
x = [1, 2]
y = x
if x is y:
    print("Address:", id(x))
else:
    print("x:", id(x), "y:", id(y))

#60 Special Symbol Check
ch = "#"
if not ch.isalnum():
    print(ch * 3)
    print(ch * 5)

#61 Equal Length String Collections
a = "abc"
b = "xyz"
if len(a) == len(b):
    print(a + b)
else:
    print(a, b)

#62 Same Memory Location: Print Last or First + Address
a = [1, 2, 3]
b = a
if a is b:
    print(b[-1])
else:
    print(a[0], id(a))

#63 String Print 5 Times or 3 Times Based on Conditions?????????????????
s = "hello"
vowels = 'aeiouAEIOU'
if len(s) > 3 and s[len(s)//2] in vowels:
    if ord(s[0]) % 2 == 0:
        print("Previous of middle:", s[len(s)//2 - 1])
    else:
        print(s * 3)
else:
    print(s * 5)
#--------------------------page 5 --------------------------------------------------
#64 Ravi's Red Pen Buying Decision
pen_available = True
pen_cost = 10

if pen_available and pen_cost == 10:
    print("Ravi will buy the pen.")
else:
    print("Ravi will come out of the shop.")


#65 List Addition or Subtraction Based on Even Numbers
data = [2, 7, 4, 9, 6]
first = data[0]
middle = data[len(data)//2]
if first % 2 == 0 and middle % 2 == 0:
    result = first + middle
    print("Addition result:", result)
else:
    result = first - middle
    print("Subtraction result:", result)


#66 First Item of Two Lists – Type Check
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
if isinstance(list1[0], int) or isinstance(list2[0], int):
    combined = list1 + list2
    print("Concatenated List:", combined)
else:
    print("Memory addresses:", id(list1), id(list2))
    
'''