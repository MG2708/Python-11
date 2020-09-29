#5 random numbers between 2
import random
def ran(x,y):
    for i in range(5):
        i=random.randrange(x,y)
        print(i)        
            
a=int(input("Enter lower limit : "))
b=int(input("Enter upper limit : "))
print()
print("Five random numbers between entered limit are : ")
ran(a,b)
            
