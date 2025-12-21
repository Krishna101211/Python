import re
'''
#match()------> new_var=re.match(pattern,source_of_string)
y="Good evening"
z=re.match("Good",y)
print(z)
print(z.start())
print(z.end())
print(http://z.group())
'''
'''
y="Good evening"

#fullmatch()------> new_var=re.fullmatch(pattern,source_of_string)
w=re.fullmatch("Good evening",y)
print(w)
print(w.start())
print(w.end())
print(http://w.group())
'''

'''
#search():----->
#new_var=http://re.search("Pattern",source_of_string)
y="Good evening"
http://e=re.search('o',y)
print(e)
http://e1=re.search('evening',y)
print(e1)
'''
y="Good evening"

'''
u=re.finditer("e",y)
for i in u:
    print("e------------>",i)

u=re.finditer("e",y)
print(list(u))
'''
'''
u="yellow"

t=re.sub("l","*",u,1000)
print(t)

t1=re.subn("l","*",u,1000)
print(t1)

'''
'''
t="good morning"
x=re.split("o",t,1)
print(x)
y=re.split("n",t,1)
print(y)
'''




#findall()

#new_var=re.findall("pattern",source_of_string)

s="HELLO guys welcome @#$%^&*()(*&^TO all 2345678"
'''
k=re.findall('[A-Z]',s)
print(k)

k=re.findall('[A-Z]+',s)
print(k)
'''
# r=re.findall('[a-z]+',s)
# print(r)
#
# r1=re.findall('[A-Za-z]+',s)
# print(r1)
'''
r=re.findall('[0-9]+',s)
print(r)

r1=re.findall(r"\d+",s)
print(r1)

r2=re.findall(r"\D",s)
print(r2)
'''