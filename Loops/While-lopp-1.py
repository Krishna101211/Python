"""
x=[1,2,3,4,5,6]
i=0
sum=0
while i<len(x):
        sum=sum+x[i]
        i+=1
print(sum)

y=" India won the cup in month of august 15"
i=0
v='aeiouAEIOU'
n=0
while i<len(y):
    if y[i] in v or y[i].isdigit():
        print(n)

x=[12,34,78.90,"abc",'xyz','hero',[1,2,3,'mno','PQR']]
i=0
while i<len(x):
    if isinstance(x[i],list):
            a=x.pop(i)
            b=x+a
            print(b)
    i=i+1

#wap print 0 to 20 even=[] and odd=[]
e=[]
o=[]
i=0
while i<=20:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
    i=i+1
print(e)
print(o)

# print number 10,20,30 to 300
i=10
z=[]
while i<300 :
    i=i+10
    z.append(i)
print(z)"""
#wap to find substring character in position

w='Good evening'
y=eval(input())
i=0
while i<len(w):
    if y in w[i]:
        print(i)
    i=i+1

