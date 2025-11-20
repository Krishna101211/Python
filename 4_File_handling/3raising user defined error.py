"in first one we are handling error after raising in 2nd one we are handling error before raising "
'''

'''
class NegativeError(BaseException):
    pass
def Demo(s):
    if s>0:
        print("its a +ve number")
    else:
        raise NegativeError
Demo(50)
Demo(-50)
'''

'''

class Length_error(Exception):
    ...

def Password(s):
    if len(s)>=6:
        print("valid Password length")
    else:
        raise Length_error
Password('1234567')
Password('12345')

'''

'''
class PalindromeError(BaseException):
    pass

def Display(r):
    if r==r[::-1]:
        return True,r
    else:
        raise PalindromeError
z1=Display("Python")
print(z1)
'''

'''
d=[1,2,3,4]
try:
    print(d[100])
except:
    print("error Handling")
'''

'''
class PalindromeError(BaseException):
    pass
def Display(r):
    if r==r[::-1]:
        print("its a palindrome")
    else:
        raise PalindromeError
try:
    Display("Python")
except:
    print("error Handling")

'''


"""
assert:-->
syntax:--> assert condition message

x=10
assert x>0
print("working")

print()

x=-10
assert x>0
print("working")

l=[1,2,3,4]
assert len(l)>0
print("list have some element")

l=[]
assert len(l)>0
print("list have some element")


marks=int(input("enter the number"))
assert 0<=marks<=85
print("good marks")

'''
# 1. Define user-defined exceptions
class NegativeNumberError(Exception):
    """Raised when a negative number is used."""
    pass

class DivisionByZeroError(Exception):
    """Raised when trying to divide by zero."""
    pass

class ValueTooLargeError(Exception):
    """Raised when a value is too large."""
    pass

class InvalidNameError(Exception):
    """Raised when the name contains invalid characters."""
    pass


# 2. Example usage of the custom errors
def process_number(num):
    if num < 0:
        raise NegativeNumberError("Number cannot be negative!")
    if num == 0:
        raise DivisionByZeroError("Division by zero is not allowed!")
    if num > 1000:
        raise ValueTooLargeError("Number is too large!")
    return 100 / num


def process_name(name):
    if not name.isalpha():
        raise InvalidNameError("Name must contain only alphabets!")
    return name.upper()


# 3. Test the exceptions
try:
    print(process_number(-5))        # Raises NegativeNumberError
except Exception as e:
    print(f"Error: {e}")

try:
    print(process_number(0))         # Raises DivisionByZeroError
except Exception as e:
    print(f"Error: {e}")

try:
    print(process_number(2000))      # Raises ValueTooLargeError
except Exception as e:
    print(f"Error: {e}")

try:
    print(process_name("John123"))   # Raises InvalidNameError
except Exception as e:
    print(f"Error: {e}")


