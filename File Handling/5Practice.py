#question link--->
# https://pynative.com/python-file-handling-exercises/#h-exercise-1-read-a-file
import os
# data= open("sample.txt",'r',newline='')
# print(data.readline())
# os.popen("sample.txt")

# with open("sample.txt","r")as d:
#     new=d.read()
# os.popen("sample.txt")

"how to read line by line "
# try:
#     with open("sample.txt", 'r') as file:
#         for line in file:
#             print(line, end='') # The 'end=''' prevents extra newline characters
# except FileNotFoundError:
#     print("Error: 'sample.txt' not found.")

"read top 5 lines"
try:
    with open("sample.txt", 'r') as file:
        for i in range(5):
          print(file.readline().strip())
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")