#ex1
k={1:2,67:89,100:"hi"}
try:
    print(k.append())

except AttributeError:
    print("AttributeError Handled")

except KeyError:
    print("Key error handled")

except TypeError:
    print("Type error handled")

except NameError:
    print("Name error Handled")

#ex--->2
k={1:2,67:89,100:"hi"}
try:
    print(k.append())
except (NameError,FileExistsError,TypeError,ValueError):
    print("Error done ")
'''
#
# s=[1,2,3,4,5]
# try:
#     print(s.remove(15))
# except KeyError:
#     print("Key error")
# except IndexError:
#     print("Index error")
# except ValueError:
#     print("value error")

'''
s=[1,2,3,4,5]
try:
    print(s.remove(15))
except Exception as msg:
    print(msg)
    print("error Handled")

print("---------------------------->>>>>")
r="Hello"
try:
    print(r.append())

except BaseException as x:
    print("Error done")
    print(x)
'''

"""
combination of try block and except and else block and finally block

syntax:--->

try:
    statement/Error_line
except Exception_Name:
    statement
else:
    statement        
"""
# try:
#     a=int(input("enter the number"))
#     print(a)
#
# except ValueError:
#     print("value error done")
#
# else:
#     print("No error Guys")
# finally:
#     print("@#$%^&*()_")

'''
try:
    print("Hello".append())

    try:
        print("Hero".append())

    except AttributeError:
        print("AttributeError Done")
    else:
        print("checking")
    finally:
        print("no error")
except:
    print("error Done")
else:
    print("checking done")
finally:
    print("*******")

'''




"""
class userdefined_error_Name(BaseException):
            pass/...
        statement           
"""
'''
class Mobile_Error(BaseException):
    pass
def Mobile(num):
    if len(num)==10:
        print("valid mobile number")
    else:
        raise Mobile_Error
# Mobile("1234567896")
Mobile("123456789")
'''
'''
class Negative_Error(BaseException):
    pass
def Mobile(num):
    if num>0:
        return True,"+ve number"
    else:
        raise Negative_Error
m=Mobile(-10)
print(m)
'''

#How to Handled userdefined Error-------------------->>???
class Negative_Error(BaseException):
    ...
def Mobile(num):
    if num>0:
        return True,"+ve number"
    else:
        raise Negative_Error
try:
    print(Mobile(10))
except BaseException as e:
    print("Error Handled")
'''