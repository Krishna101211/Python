'''
#Write a program that prints numbers from 1 to 10 using a while loop.
i=0
while i<=10:
    print(i)
    i+=1

#Use a while loop to print all even numbers between 1 and 20.
i=0
while i<=20:
    if i%2==0:
        print(i)
    i+=1

#Use a while loop to calculate the sum of numbers from 1 to 100.
i=0
s=0
while i<=101:
    print(s)
    s=s+i
    i+=1

#Ask the user for a number n, then print a countdown from n to 1.
x=int(input())
while x>=1:
    print(x)
    x=x-1


#The program chooses a number (say 7). Keep asking the user to guess until they get it right.
y = int(input())
if y == 7:
    print(" You predict correct number i.e 7")
else:
    i=0
    while y<7 or y>7:
        y = int(input(f"Please enter correct num\n"))
    i+=1

#Use a while loop to compute the factorial of a number n
n = int(input("Enter a number: "))
result = 1
while n > 0:
    result *= n
    n -= 1
print("Factorial =", result)

#Take an integer input and use a while loop to reverse its digits. Example: 1234 → 4321
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10      # get the last digit
    rev = rev * 10 + digit  # add it to reversed number
    num = num // 10       # remove the last digit

print("Reversed number:", rev)

#Input a number and use a while loop to find the sum of its digits.
# Take input from user
num = int(input("Enter a number: "))

# Variable to store sum
digit_sum = 0

# Loop until number becomes 0
while num > 0:
    digit = num % 10        # get the last digit
    digit_sum += digit      # add it to sum
    num = num // 10         # remove the last digit

print("Sum of digits:", digit_sum)
'''
