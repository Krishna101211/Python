'''x=(1,2,3,4,5)
y=()
for i in range(-1,-len(x)-1,-1):
    print(x[i])

for i in reversed(x):
    print(i)

for i in x:#without using inbuilt function
    y=(i,)+y
    print(y,end="")

for i in x[::-1]:#used slicing
    print(i,end="")
'''
