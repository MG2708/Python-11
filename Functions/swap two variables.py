#Swap two variables
def swap(x,y):
    t=x
    x=y
    y=t
    print("AFTER FUNCTION CALL, value of x is :",x,"and of y is :",y)
x=int(input("Enter a value : "))
y=int(input("Enter another value : "))
print("Value of x is :",x,"and of y is :",y)
swap(x,y)


