#Print sum of all even and odd numbers upto user entered number
esum=0
osum=0
g=int(input("Upto Which number :"))
m=1
while m<=g:
    if m%2==0:
        esum+=m
    else:
        osum+=m
    m=m+1
print("The sum of all even numbers upto(including)",g," is : ", esum)
print("The sum of all odd numbers upto(including)",g," is : ", osum)

    
    
