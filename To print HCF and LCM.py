#To print HCF 
x=int(input("Enter a number : "))
y=int(input("Enter another number : "))
if (x>y):
    smaller=y
else:
    smaller=x
for i in range (1,smaller+1):
    if (x%i==0) and (y%i==0):
        hcf=i
print("The HCF is : ",hcf)

#To print LCM
lcm=(x*y)//hcf
print("The LCM is : ",lcm)
