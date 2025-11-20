"""
# 1.Write a program that divides two numbers and handle ZeroDivisionError.
a=2
b=0
try:
    print(a/b)

except:
    print("zero division error")

# 2.Write a program that reads a number from the user,
# convert it to integer, and handle ValueError if input is invalid.

try:
    x = int(input("please enter the number only:"))
    print(x)
except ValueError:
    print("wrong input ")

# 3.Write a program to open a file and handle FileNotFoundError
#  if it doesn’t exist.
try:

    with open("File.txt", "r") as f:
        content = f.read()
        print("File content:\n", content)

except FileNotFoundError:

    print("Error: The file 'File.txt' was not found.")

# 4.Write a program to demonstrate try-except-else
#  where else executes only when no exception occurs.
a=2
b=3
try:
    print(a/b)
except:
    print("Error occur")
else:
    print("No exception occur")

# 5.Write a program to demonstrate try-finally where
# finally always executes, even if error occurs.
a=2
b=0
try:
    print(a/b)
except:
    print("Error occur")
else:
    print("No exception occur")
finally:
    print("This division code")

from operator import index


# 6.Write a program that catches multiple exceptions
# (ValueError and TypeError) separately.

try:
    x=input("enter the value")
    y=input("enter number")
    print(x+y)
except ValueError:
    print("value error handled")
except TypeError:
    print("type error  handled")

# 7.Write a program that shows the difference between
# catching Exception and BaseException.

#8.Write a program to handle IndexError
#  while iterating through a list beyond its length.

# 9.Write a program to handle KeyError when
#  accessing a dictionary key that does not exist.
x={9:4,5:6}

try:
    x[6]
except KeyError :
    print("handled key error ")



# 10.Write a program to handle AttributeError
# when accessing an attribute that does not exist.
l="hii"
try:
    l.append(4)
except AttributeError:
    print("attribute error handled")


# 11.Write a program that demonstrates
# assertion error using assert.

# 12.Write a program that shows how finally
#  executes even when a function uses return statement.
def hello():#when we dont want to use except block we go for function format
    try:
        return "My name is hello"
    hello()

    # except:
    #     print("error occurs")
    finally:
        print("This is function code")

# 13.Write a program that catches StopIteration
#  when using next() on an empty generator.

# 14.Write a program that tries to
# import a non-existing module and handle ModuleNotFoundError.
try:
    import krishnashinde
except ModuleNotFoundError:
    print("handled Module not found error")

# 15.show me one example on combination of try
# and except and else and finally in nested
# try and except block
try:
    x=int((input("Enter 1st number:")))
    y= int((input("Enter 2nd number:")))

    try:
        print(x/y)
    except ZeroDivisionError:
        print("division error happend")
    else:
        print("divison happend vale is",x/y)
    finally:
        print("Please enter the 2nd number non zero")

except:
    print("Your not enter number format")
"""
'''
class Negative_error(BaseException):
    pass
def Number(x):
    if x>0:
        print("its a +ve number")
    else:
        raise Negative_error ("The give number is -ve")
try:
    Number(10)
except BaseException as e:
    print("error handled")
    print(e)
'''