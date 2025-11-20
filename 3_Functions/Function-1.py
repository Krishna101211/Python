'''
def demo(a,b,c):
    print(a,b,c)
demo(1,2,3)


def demo(a,b):
    print(a,b)
demo(1,2)

def demo(*args,**kwargs):
    print(args,kwargs)
demo()
demo(1,2,45,44)
demo(1,23,4,5,[1,23,45],x=90,y=25,z='hii',a=[1,23,4,5])

def check(*args,**kwargs):
    print(args,kwargs)
check()
check(1,2,3,4)

def call(*args):
    total=0
    total=total+1
    return total

x=call(1,2,34,5,6)
print(x)


def call(*args):
    total=0
    total = total + 1
    print(total)

call('a','b',1,2,34,5,6)

def square(l):
    k=[]
    for i in l:
        k.append(i**2)
    print(k
          )
square([1,2,3])

def read(a,b,c):
    k=a+b
    print(k)
    l=k-c
    print(l)
read(10,20,10)

def alphabet(l):
    if l.isalpha():
        print("TYpe of given input is int ")
    elif l.isdigit():
        print("all are digits ")
    else:
        print("special character")


def slicing(l):
    print(l[0::2])
slicing('TRACXN')

def slicing(l,k):
    return(l[k::2])
z=slicing('TRACXN',1)
print(z)


def position(l,k):
    if len(l)>=k:
        print(f"given string length greater than {k}")
    else:
        print(f"given value is smaller than {k}")
position("hell",5)

def question(s):
    k={}
    for i in s:
        k[i]=[ord(i)]
    print(k)
question("ITs yours day")

1. Function to search for a character in a string and return its index
def search_char(string, ch):
    for i in range(len(string)):
        if string[i] == ch:
            return i
    return -1   # if not found

# Example
string = "coding part is done"
print(search_char(string, "p"))   # Output: 7

2. Check if a given character is alphabet, digit, or special character (without inbuilt)
def check_char(ch):
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        return "Alphabet"
    elif '0' <= ch <= '9':
        return "Digit"
    else:
        return "Special Character"

# Example
print(check_char("A"))   # Alphabet
print(check_char("9"))   # Digit
print(check_char("@"))   # Special Character

3. Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example
print(is_prime(7))   # True
print(is_prime(10))  # False

4. Return length of an iterable without using len()
def get_length(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count

# Example
print(get_length([1, 2, 3, 4]))   # 4
print(get_length("hello"))        # 5

5. Count number of arguments passed (positional & keyword)
def count_args(*args, **kwargs):
    return len(args) + len(kwargs)

# Example
print(count_args(1, 2, 3, a=10, b=20))  # 5 (3 positional + 2 keyword)

'''