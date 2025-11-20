"""
                    lambda syntax
syntax1
new_var_name=lambda arg1,arg2,arg3........:expression
print(new_var_name)  #object address
print(new_var_name(value1,value2......))

syntax2:->
new_one=lambda arg1 :TSB if condition else block
print(new_one())

syntax3:-->
new_one=lambda arg1.... :[expression for loop condition]

"""
'''
def spam():
    print("evening")
print(spam) #<function spam at 0x0000026A522E4AE0>
spam()


x=lambda :"evening"
print(x)  #<function <lambda> at 0x000001A6C469F9C0>
print(x())


y=lambda i,j:i*j
print(y(4,5))
'''

s=25
'''
syntax2:->
new_one=lambda arg1 :TSB if condition else block
print(new_one())
'''

'''
a=lambda s:f'The given number {s} is a even number ' if s%2==0 else f'The given number {s} is a odd number '
print(a(25))
print(a(22))


e=4
d=lambda e:(e**2,e**3)
print(d(4))

'''


w="Python"

# e=lambda w:(len(w),w)
# print(e("Python"))

# e1=lambda w:((len(w),w),{len(w):w})
# print(e1("Python"))


k=["apple","iphone","mack"]
"""
syntax3:-->
new_one=lambda arg1.... :[expression for loop condition]
"""
# q=lambda k:[i[0] for i in k]
# print(q(["apple","iphone","mack"]))

# q1=lambda k:[i for i in enumerate(k)]
# print(q1(["apple","iphone","mack"]))

# q2=lambda k:[(i,j) for i,j in enumerate(k)]
# print(q2(["apple","iphone","mack"]))

# e=[10,15,17,18,29,30]
# for i in e:
#     if i%5==0:
#         print(i)
#     else:
#         print(i**2)

# r=lambda e:[i  for i in e if i%5==0]
# print(r([10,15,17,18,29,30]))

# r1=lambda e:[i if i%5==0 else i**2 for i in e]
# print(r1([10,15,17,18,29,30]))



# # 1. add two numbers
# add = lambda a,b: a+b
# print(add(10,20))  # 30
#
# # 2. multiply two numbers
# mul = lambda a,b: a*b
# print(mul(5,4))  # 20
#
# # 3. find maximum of two numbers
# maximum = lambda a,b: a if a>b else b
# print(maximum(10,20))  # 20
#
# # 4. find minimum of two numbers
# minimum = lambda a,b: a if a<b else b
# print(minimum(10,20))  # 10
#
# # 5. square of a number
# square = lambda x: x**2
# print(square(6))  # 36
#
# # 6. cube of a number
# cube = lambda x: x**3
# print(cube(3))  # 27
#
# # 7. check even number
# is_even = lambda x: x%2==0
# print(is_even(4))  # True
#
# # 8. Absolute value
# absolute = lambda x: x if x>=0 else -x
# print(absolute(-9))  # 9
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # 9. greater among three numbers
# max_three = lambda a,b,c: max(a,b,c)
# print(max_three(10,20,30))  # 30

# # 10. length of a string
# str_len = lambda s: len(s)
# print(str_len("python"))  # 6
#
# # 11. Reverse a string
# reverse_str = lambda s: s[::-1]
# print(reverse_str("hello"))  # olleh
#
# # 12. Palindrome check
# is_palindrome = lambda s: s==s[::-1]
# print(is_palindrome("madam"))  # True
#
# # 13. find largest word in a string
# largest_word = lambda s: max(s.split(), key=len)
# print(largest_word("python is powerful"))  # powerful
#
# # 14. Last digit of a number
# last_digit = lambda n: n%10
# print(last_digit(789))  # 9
#
# # 15. First digit of a number
# first_digit = lambda n: int(str(n)[0])
# print(first_digit(789))  # 7
#
# # 16. Swap two numbers
# swap = lambda a,b: (b,a)
# print(swap(10,20))  # (20, 10)
#
# # 17. Leap year check
# is_leap = lambda y: (y%4==0 and y%100!=0) or (y%400==0)
# print(is_leap(2024))  # True
#
# # 18. String uppercase
# to_upper = lambda s: s.upper()
# print(to_upper("python"))  # PYTHON
#
# # 19. Title case string
# to_title = lambda s: s.title()
# print(to_title("hello world"))  # Hello World
#
# # 20. Count words in a string
# word_count = lambda s: len(s.split())
# print(word_count("python is great"))  # 3
#
# # 21. number divisible by both 3 and 7
# div_3_7 = lambda x: x%3==0 and x%7==0
# print(div_3_7(21))  # True
#
# # 22. Square root of a number
# sqrt = lambda x: x**0.5
# print(sqrt(16))  # 4.0
#
# # 23. Rectangle area
# rect_area = lambda l,w: l*w
# print(rect_area(5,4))  # 20
#
# # 24. Circle area
# circle_area = lambda r: 3.14159*r*r
# print(circle_area(3))  # 28.27431
#
# # 25. Concatenate two strings
# concat = lambda a,b: a+b
# print(concat("Hello","World"))  # HelloWorld
#
# # 26. Repeat string n times
# repeat = lambda s,n: s*n
# print(repeat("Hi",3))  # HiHiHi
#
# # 27. Check substring present
# has_sub = lambda s,sub: sub in s
# print(has_sub("python","tho"))  # True
#
# # 28. Find the largest of four numbers
# max_four = lambda a,b,c,d: max(a,b,c,d)
# print(max_four(10,40,30,20))  # 40
#
# # 29. return the keys of a dictionary
# dict_keys = lambda d: list(d.keys())
# print(dict_keys({"hello":"Sony","How":"are","you":"bye"}))
# # ['hello','How','you']
#
# # 30. first element of a sequence
# first_elem = lambda seq: seq[0]
# print(first_elem([10,20,30]))  # 10
#
# # 31. length of any iterable
# iter_len = lambda x: len(x)
# print(iter_len((1,2,3,4)))  # 4
#
# # 32. list of squares of numbers
# squares_list = lambda l: [x**2 for x in l]
# print(squares_list([2,3,4,5,6]))
# # [4,9,16,25,36]
#
# # 33. numbers with indices pair
# index_pairs = lambda l: list(enumerate(l))
# print(index_pairs([100,200,300]))
# # [(0,100),(1,200),(2,300)]
#
# # 34. check if data is sequence
# check_seq = lambda x: ("length",len(x)) if hasattr(x,'__len__') else ("type",type(x))
# print(check_seq([1,2,3]))  # ('length', 3)
# print(check_seq(123))      # ('type', <class 'int'>)
#
# # 35. even or odd: even→square, odd→sqrt
# even_square_odd_sqrt = lambda x: x**2 if x%2==0 else x**0.5
# print(even_square_odd_sqrt(4))  # 16
# print(even_square_odd_sqrt(9))  # 3.0
#
# # 36. if length even return same else reverse
# even_len_same_else_reverse = lambda s: s if len(s)%2==0 else s[::-1]
# print(even_len_same_else_reverse("hello"))  # olleh
#
# # 37. return value & length in tuple & dict
# value_and_len = lambda s: ((s,len(s)), {s:len(s)})
# print(value_and_len("python"))
# # (('python',6), {'python':6})
#
# # 38. same as 34 (sequence check)
# check_seq2 = lambda x: ("length",len(x)) if hasattr(x,'__len__') else ("type",type(x))
# print(check_seq2("abc"))  # ('length', 3)
#
# # 39. divisible by 5 then +5 else -5
# plus_or_minus_5 = lambda x: x+5 if x%5==0 else x-5
# print(plus_or_minus_5(10))  # 15
# print(plus_or_minus_5(7))   # 2
#
# # 40. Check if two strings are anagrams
# is_anagram = lambda s1,s2: sorted(s1)==sorted(s2)
# print(is_anagram("listen","silent"))  # True

