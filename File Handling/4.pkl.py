"""

with using file Handling

dump()----> it will accept two arguments (iterable,file_object)
with open('file_name.pkl',"mode(wb)")as file_obejct:
    new_var=pickle.dump(iterable,file_object)


load()----> it will accept only one argument(file_object)
with open('file_name.pkl',"mode(rb)")as file_obejct:
    new_var=pickle.load(file_object)
    print(new_var)

import pickle
s="Hello Python"
with open("error.pkl","wb")as file:
    x=pickle.dump(["hello","python","data","sql"],file)
# os.popen("error.pkl")

with open("error.pkl","rb")as file:
    w=pickle.load(file)
    print(w)


without using fileHandling
dumps()
new_var_name=pickle.dumps(iterable)

loads()
new_var_name=pickle.loads(var_name)

import pickle
s="Hello Python"
x=pickle.dumps(s)  #Python to bytestream
print(x)

y=pickle.loads(x) #bytestream to Python
print(y)

"""