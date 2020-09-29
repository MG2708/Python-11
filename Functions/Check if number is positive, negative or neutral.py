#Check if number is positive, negative or neutral
def check(x):
    if x==0:
        print("Neutral")
    elif x>0:
        print("Positive")
    else:
        print("Negative")

a=int(input("Enter a number: "))
check(a)
              
