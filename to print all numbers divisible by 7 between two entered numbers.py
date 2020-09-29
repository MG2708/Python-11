#To print all numbers divisible by 7 between two numbers
m = int(input("Enter a number : "))
n = int(input("Enter a number greater than previous one : "))
for p in range(m,n+1,1):
    if p%7==0:
        print(p)
    

