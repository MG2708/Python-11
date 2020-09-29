#Scan a number and deetermine if it is positive, negative or neutral
number=float(input("Enter a number"))
if number>0:
    print("The number entered is positive")
else:
    if number==0:
        print("The number entered is neutral")
    else:
        if number<0:
            print("The number entered is negative")
        else:
            print("Entered number is false and not real")
