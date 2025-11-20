"""Tech number
A Tech Number is a number that: Has an even number of digits.
If we split it into two equal halves, add them, and square the sum,
the result is the original number
x=81
#2025 #302
y=str(x)
mid=len(y)//2
first=int(y[0:mid])
#30
second=int(y[mid:])
#25
print(first)
print(second)
if (first+second)**2==x:
    print("TechNumber")
else:
    print("its not")

x=13
sq=int((x+1)**0.5)
print(sq)
if sq*sq==x+1:
    print("sunny number")
else:
    print("its not")

import math
x=13
print(math.sqrt(x+1))
#4.0
print(math.isqrt(x+1))
if math.isqrt(x+1)**2==x+1:
    print("sunny number")
else:
    print("its not")

"""

