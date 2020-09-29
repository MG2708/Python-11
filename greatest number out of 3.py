#Enter three numbers and determine the greatest amongst them
a=float(input("Enter a number"))
b=float(input("Enter another number"))
c=float(input("Enter a last number"))
if a>b>c :
    print("The greatest number amongst entered is :", a )
else:
    if b>c:
        print("The greatest number amongst entered is :", b)
    else:
        print("The greatest number amongst entered is :", c)
        
    
