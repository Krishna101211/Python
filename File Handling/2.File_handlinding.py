import os
# print(os.getcwd())
# os.popen(r'C:\Users\prath\OneDrive\Desktop\QSPIDER\Evening.txt')
# print(os.getcwd())

#step-->1
# file=open("Evening.txt","w")
# os.popen("Evening.txt")


"""
w----> write/write mode

write mode we have two types

1.write()------> Here we can add the data(only single line)

2.writelines()---> Here we can add the data(multiple line)

syntax:---> new_var_name=open('file_name.extension','w')
            print(new_var_name.write())
            print(new_var_name.writlines(["iterable1","iterable2......])

        write_mode example:-->
-----------------------------------------------
file=open("Evening.txt","w")
# print(file.write("Good evening"))
# print(file.write("Python class"))
print(file.writelines(["Python\n","Java\n","SQL\n","web-tech\n","PowerBI\n"]))
os.popen("Evening.txt")

"""
# file=open("Evening.txt","a")
# print(file.write("Hello guys my name is"))
"""
a---> append/a_mode

1.write()------> Here we can add the data(only single line)

2.writelines()---> Here we can add the data(multiple line)

syntax:---> new_var_name=open('file_name.extension','a')
            print(new_var_name.write())
            print(new_var_name.writlines(["iterable1","iterable2......])



"""
# new_file=open("JOY.txt","w")
# print(new_file.write("firstclass\n"))
# # print(new_file.write("secondclass\n"))
# print(new_file.writelines(["XYZ\n","ABC\n","PQR\n","MnO\n"]))
# os.popen("JOY.txt")
"""
r----> read/r_mode
1.read()
2.readline()
3.readlines()
4.read(n)---> n---> number of character

syntax:---> new_var_name=open('file_name.extension','r')
            print(new_var_name.read())
            print(new_var_name.readline()
            print(new_var_name.readlines()
            print(new_var_name.read(n)

data=open("JOY.txt","r")
print(data.read())
print(data.readline())
print(data.readline())
print(data.readline())
print(data.readline())
print(data.readlines())
print(data.read(10))

"""

"""
with context manager syntax

with open('file_name.extension','mode')as file_object:
            pass
"""


'''
data=open("JOY.txt","r")
print(data.read())

#------------------------------------

with open("JOY.txt","r")as file:
    print(file.read())

'''

'''
data=open("email.txt","w")
#-----------------------------------------
with open("email1.txt","w")as file:
    pass

'''

'''
data=open("email.txt","w")
print(data.write("Joy"))
os.popen("email.txt")
------------------------------------


'''
# with open("email1.txt","w")as z:
#     print(z.writelines(["Think","study",'daily']))
# os.popen("email1.txt")

