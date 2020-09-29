#Print sum of all even and odd numbers for given two numbers by the user
esum=0
osum=0
m=int(input("Enter a  number :"))
g=int(input("Enter another number greater than previously entered : "))
while m<=g:
    if m%2==0:
        esum+=m
    else:
        osum+=g
    m=m+1
print("The sum of all even numbers in given range is : ", esum)
print("The sum of all odd numbers in given range is : ", osum)

    
    
