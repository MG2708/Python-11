 #Program to print all the Factors of a given integer
n=int(input("Enter an integer:"))
print("The Factors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=' ')
