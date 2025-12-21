import re

s='good afternoon guys all '
a=re.finditer('good',s)
# print(list(a))
# for i in a:
#     print('0-->',i)

s='good afternoon guys all '
# a=re.match('good',s)
# print(a)
# for i in a:
#     print('0-->',i)
e1=re.subn('o','*',s,0)
print(e1)


