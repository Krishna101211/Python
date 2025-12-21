"""
import csv

1.writing into csv File

    *writer()

    *Dictwriter()

 *writer()

 syntax:--->

 with open("file_name.csv","mode")as file_object:
    new_var=csv.writer(file_object)
    new_var.writerow([data])
    new_var.writerows([[data],[data2],[data3].....])
"""

import os

# print(os.getcwd())
# os.chdir(r"C:\Users\prath\OneDrive\Desktop\OSfile1")
# print(os.getcwd())
import csv

# with open("Red.csv","w",newline='')as file:
#     data=csv.writer(file)
#     # data.writerow(["RedPen",500])
#     # data.writerow(["Blue_Pen",1000])
#     data.writerows([["Red",100],["Pink",200],["yellow",300],["Blue",400]])
# os.popen("Red.csv")


# with open("Data.csv","w")as d:
#     l=csv.writer(d)
#     l.writerow(["ww",100])
# os.popen("Data.csv")


"""
Dictwriter()
with open("file_name.csv","mode")as file_object:
    new_var=csv.Dictwriter(file_object,[field_name1,field_name2.....])
    new_var.writeheader()
    new_var.writerow({field_name1:data,field_name2:dat2})
    new_var.writerows([{field_name1:data,field_name2:dat2},{field_name1:data,field_name2:dat2},{field_name1:data,field_name2:dat2}])
"""


# with open("Done.csv","w",newline='')as file:
#     new=csv.DictWriter(file,["Name","ID"])
#     new.writeheader()
#     # new.writerow({"Name":"Ram","ID":121})
#     # new.writerow({"Name":"Kiran","ID":1200})
#     new.writerows([{"Name":"Mahii","ID":101},{"Name":"Manu","ID":111},{"Name":"HP","ID":155},{"Name":"Rahul","ID":555},{"Name":"vikas","ID":777}])
# os.popen("Done.csv")


# with open("Data_base.csv","w",newline="") as D:
#     new=csv.DictWriter(D,["NAME","SAL"])
#     new.writeheader()
#     new.writerows([{"NAME":"LISA","SAL":1111},{"NAME":"BEN","SAL":10000}])
# os.popen("Data_base.csv")

"""
Reading into csv File

* reader()
*Dictreader()

with open("file_name.csv","mode")as file_object:
    new_var=csv.reader(file_object)
    print(new_var)---> object address

    #Typecasting
    print(list(new_var))

    #Looping
    for i in new_var:
        print(i)
"""


# with open("Red.csv","r")as file:
#     x=csv.reader(file)
#     # print(list(x))
#     for i in x:
#         print(i)

# with open("Done.csv","r")as file:
#     k=csv.DictReader(file)
#     # print(list(k))
#     for i in k:
#         print(i)


# with open("Red.csv","r")as file:
#     x=csv.DictReader(file)
#     for i in x:
#         print(i)

import csv
# with open("Red.csv","w",newline='')as file:
#     data=csv.writer(file)
#     data.writerow(["RedPen",500])
#     data.writerow(["Blue_Pen",1000])
#     data.writerows([["Red",100],["Pink",200],["yellow",300],["Blue",400]])
# os.popen("Red.csv")


# with open("car.csv","w",newline='')as file:
#     file= csv.writer(file, ["Car_Name", "Car_model"])
#     # file.writeheader()
#     file.writerow(["Lamorgni",'540'])
#     file.writerow(["Jagvar",'120'])
#     file.writerows([["Ferrari",100],["Pink",200],["yellow",300],["Blue",400]])
# os.popen("car.csv")


# with open('Colour.csv','w',newline='')as c:
#     Co=csv.DictWriter((c,['COLoure','Rating']))
#     Co.writeheader()
#     Co.writerow({'red':'4','blue':'3'})
# os.popen('Colour.csv')


# with open("file_name.csv","mode")as file_object:
#     new_var=csv.Dictwriter(file_object,[field_name1,field_name2.....])
#     new_var.writeheader()
#     new_var.writerow({field_name1:data,field_name2:dat2})
#     new_var.writerows([{field_name1:data,field_name2:dat2},{field_name1:data,field_name2:dat2},{field_name1:data,field_name2:dat2}])