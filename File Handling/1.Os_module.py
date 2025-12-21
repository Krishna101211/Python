#will rmdir remove folder contain also or just folder ???
"""
osmodule------> step1---> import os

1.getcwd()---> print(os.getcwd())

2.chdir()----> os.chdir(r'Path')

3.mkdir()----> os.mkdir('folder_name')

4.rmdir()----> os.rmdir("Folder_name") #only folder can delete

5.remove()----> os.remove('File_name.extension') #only file

6.listdir()----> print(os.listdir()) complete information of the folder.

7.rename()----> os.rename('old_name','new_name')

8.popen()-----> os.popen('File-name.extension')

Note:---> To avoid special sequence we have to use--->r---> raw string
          else----> singleslash make it has a double slash
"""

# import os
# x=os.listdir(r"C:\Users\prath\OneDrive\Desktop\QSPIDER\File_handling")
# print(x)
#o/p--->['1.Os_module.py', '2.File_handlinding.py', '3.csv_handling.py', '4.pkl.py', 'Attentions (mistake).txt', 'email1.txt', 'Evening.txt', 'file', 'JOY.txt']


# print(os.mkdir(r"C:\Users\prath\OneDrive\Desktop\OSfile1.txt"))
# print(os.rmdir(r"C:\Users\prath\OneDrive\Desktop\OSfile1.txt"))
# print(os.remove(r"C:\Users\prath\OneDrive\Desktop\OSfile1.txt\OSfile.txt"))
# print(os.popen('OSfile1.txt'))
