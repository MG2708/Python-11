#factorial
def fact(x):
    f=1
    if x==0:
        return 1
    else:
        while x:
            f=f*x
            x-=1
        return f
n=int(input("Enter a number: "))
print(fact(n))
