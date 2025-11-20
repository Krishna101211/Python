'''
nums=[10,20,-3,40]
for i in nums:
    if i<0:
        break
    print(i)

I=[1,2,3,4,5,6]
sum=0
for i in I:
    sum+=i:
    if sum>15:
        break
    print(i)

lst=[4,5,7,2]
for i in lst:
    if  i==9:
        break
    print(i)

s='python'
v='aeiou'

for i in s:
    if i in v:
        break
    print(i)
'''

#_____________________Continue_____________________
'''
nums=[10,20,-3,40]
for i in nums:
    if i<0:
        continue
    print(i)

s='python'
v='aeiou'
for i in s:
    if i in v:
        continue
    print(i)


for i in range(0,12):
    if i%2==1:
        print(i)
    else:
         continue

for i in range(1,22):
    if i%3==0:
        print(i)
    else:
         continue

s="PyThon"
for i in s:
    if i.isupper():
        continue
    else:
        print(i)

L=[1,2,3,10,22,33]
for i in L:
    if i >=10:
        continue
    else:

        print(i)

s="Hello python world "
c="y"
for i in s:
    if i==c:
        break
    else:
        print(i, end='')

s='good morining pune '
v='aeiou'
for i in s:
    if i in v:
        continue
    print(i, end='')
'''