#program to print sum of all digits of a given number
import math 
m=int(input("Enter a number : "))
sum=0
while m!=0:
    g=m%10
    sum=sum+g
    m=int(m/10)
ans=int(sum)
print("The sum of the digits of given number is : ",ans)
