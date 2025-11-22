"""
x=[1,2,3,4,5]
for i in x:
    print(i,end=' ')
explanation
for 1 in [1,2,3,4,5]--->True 
for 2 in [1,2,3,4,5]--->True
for 3 in [1,2,3,4,5]--->True
for 4 in [1,2,3,4,5]--->True
for 5 in [1,2,3,4,5]--->True
ex-->2
y=(11,"hello",[1,2,3],{3,4,5})
for i in y:
    print(i,end=" ")

r={1:2,45:100,"a":"b"}
for j in r:
    print(j)
print()
for j in r.values():
    print(j)

print()

#without using inbuilt to print values
for j in r:
    print(r[j])   #var_name[key]----> r[j]

print()
for j in r.items():
    print(j)
print()
##without using inbuilt to print key and values
for j in r:
    print(j,r[j])
"""

# e=[1,2,3,4,5,6,7]
# for i in e:
#     if i%2==1:
#         print(i)

# t=["python","java","sql","hi","a"]
# for i in t:
#     if len(i)%2==0:
#         print(i)
''' 
for "python" in t: 
    if len('python')%2==0: if 6%2==0:--->True  

for "java" in t: 
    if len("java")%2==0:  if 4%2==0:--->True 

for "sql" in t:         
    if len('sql')%2==0:   if 3%2==0:--->False 

for "hi" in t: 
    if len('hi')%2==0 :   if 2%2==0 :--->True 

for "a" in t: 
    if len("a")%2==0 :   if 1%2==0 :--->False 

output:--> Python,java,hi             
'''

# w="evening"
# d={}
# for i in w:
#     d.update({i:ord(i)})  #with using inbuilt function
# print(d)


# d={}
# for i in w:
#     d[i]=ord(i)
# print(d)

# wap to print vowels and number
# s="hello123"
# for i in s:
#     if i in "aeiouAEIOU" or i.isdigit():
#         print(i)


# s=[1,2,3,4,5]
# l=[]
# for i in s[::-1]:
#     l.append(i)
# print(l)

# print()
# s=[1,2,3,4,5]   #without using inbuilt function
# l=[]
# for i in s:
#     l=[i]+l
# print(l)

# x="good luck"
# for i in x[::-1]:
#     print(i,end=" ")


# res=''
# for i in x:
#     res=i+res
# print(res)