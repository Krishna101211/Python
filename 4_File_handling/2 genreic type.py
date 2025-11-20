"""
                    Generic except Block:--->
--------------------------------------------------------------------------
* Handled all kind of error

*In Generic except Block we can find the reason for error

#syntax:-->
try:
    Risky_Code/Error_Line

except Exception as msg:
    statement
    print(msg)

"""

s = "Good Morning"
'''
try:
    print(s.append())

except:
    print("error Handled")


try:
    print(s.append())

except AttributeError:
    print("AttributeError Handled")

Ex-->1
try:
    print(s.append())

except Exception as msg:
    print("Error Handled")
    print(msg)


s=11
d=0

try:
    print(s/d)
except Exception as x:
    print(x)


s=11
d=0

try:
    print(s/d)
except BaseException as x:
    print(x)
'''

# Combination of try ,except and else block

# syntax:-->
"""
try:
    RiskyCode

except:
    statement

else:
    statement        

a=11
b=3
try:
    print(a/b)   #print(11/3)

except:
    print("error done")

else:
    print("No error")

print()

try:
    print(a/c)   #print(11/3)

except:
    print("error done")

else:
    print("No error")

"""

'''
#combination of try,except,else and finally block
a=11
b=3
try:
    print(a/c)   #print(11/3)

except:
    print("error done")

else:
    print("No error")

finally:
    print("Code_Loading.......")

print()

a=11
b=3
try:
    print(a/b)   #print(11/3)

except:
    print("error done")

else:
    print("No error")

finally:
    print("Code_Loading.......")

'''

# nested try and except block

"""

try:
    Error_line

    try:
        Error_line

    except Error_name:
        statement

except Error_name:
        statement               

s="Morning"

try:
    print(s.upper())
    try:
        s.clear()
    except AttributeError:
        print("AttributeError Handled")
except:
    print("No error")

print()

try:
    s.clear()
    try:
        print(s.upper())
    except:
        print("No error")
except AttributeError:
    print("AttributeError Handled")

"""

'''
#in nested try and except block we are using else and finally block
a={1:2,67:89,100:200}
try:
    print(a[800])
    try:
        print(a[1])
    except:
        print("No error")
except KeyError:
    print("Key error")
else:
    print("error---??????")
finally:
    print("no error guys")

print()

a={1:2,67:89,100:200}
try:
    print(a[1])
    try:
        print(a[555])
    except KeyError:
        print("Key error")
    else:
        print("error---??????")
    finally:
        print("no error guys")
except:
    print("cool")
else:
    print("as of now no error")
finally:
    print("its working")

'''

