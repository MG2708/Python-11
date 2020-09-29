#Bill after appropriate discount

a=float(input("Sales:"))

if a <= 1000:
    b= a -(a/10)
    print("Your bill is",b)
elif a>= 1001 and a<=2000:
    b= a-(a/5)
    print("Your bill is",b)
else:
    b=a-(a/4)
    print("Your bill is",b)
