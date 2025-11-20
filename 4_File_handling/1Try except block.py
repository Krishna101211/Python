"""
    all language's  common error

    1.syntax error

    2.Runtime error

"""
"""
        Runtime error types

        1.predefined error

        2.userdefined error


1.predefined error :--> inbuilt error and we can't change the error name also

example---> value error,index error,key error,Type error


2.userdefined error :--> we are the user we only creating the error 
                         by the help of raise keyword

example:--> Metro error,Pen error,Phone error,Positive error                             

"""
'''
a=10
b=2

try:
    print(a/b)

except:
    print("error Handled")
'''

"""
    Types of except blocks

    1.default except block

    2.specific except block

    3.multiple except block

    4.Generic except block


 1.default except block :--->

 when we don't know what kind of error  it will occur that time we have 
 to  go for  default except block

 #syntax:--->

 try:
    Risky code/errorLine

 except:
      statement/Problem_solving

x=100
y=0
try:
    print(x/y)  #Error _line
except:
    print("Error Done")


s=(1,2,3,4,5,6)
try:
    print(s[14])
except:
    print("problem solved")


e={12:56,89:100,200:300,"a":"b"}
try:
    print(e[1200])
except:
    print("error done")

try:
    file=open("Python_class.txt","r")
except:
        print("file Operation")

"""

"""
specific except Block:-->

when we know what kind of error  it will occur that time we have 
to  go for  specific except Block


syntax:-->
try:
    Risky_code/error_line

except Error_Name:
    statement   

m=10
y=0

try:
    print(m/y)

except ZeroDivisionError :
    print("ZeroDivisionError_Handled")



r={12:45,89:900}
try:
    print(r.add(100))

except AttributeError:
    print("AttributeError handled")

try:
    file=open("Python_class.txt","r")
except FileNotFoundError:
        print("FileNotFoundError Handled")

"""

"""
3.Multiple except block
* By using single try block we can execute multiple except block
syntax:-->
try:
    Error_line/Risky_code
except Exception_Name:
    statement 
except Exception_Name:
    statement  
except Exception_Name:
    statement  
except Exception_Name:
    statement  


syntax:-->2

try:
    error_line

except (error1,error2,error3,error4...........)
    statement

example:-->

s=[1,2,3,4]
try:
    s.upper(45)
except ZeroDivisionError:
    print("error1")
except TypeError:
    print("error2")
except KeyError:
    print("error3")
except AttributeError:
    print("error4")
except ValueError:
    print("error5")


w=[11,12,13,14]
try:
    w.remove(67)

except KeyError:
    print("KeyError Handled")

except IndexError:
    print("Index error Handled")

except ValueError:
    print("value error handled")

except FileNotFoundError:
    print("file not foundError Handled")


w=[11,12,13,14]
try:
    w.remove(67)

except (KeyError,ValueError,IndexError,AttributeError,FileNotFoundError,LookupError):
    print("error solved")

"""



'''
try:
    print(10/0)
except (SyntaxError,AttributeError,ZeroDivisionError) :
    print("Error1")
'''