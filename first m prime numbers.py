m=int(input("Enter numbers to print: "))
list=[]
a=[]
length=len(list)
for val in range(1000000000):
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            list+=[val]
            length=len(list)
            if length > m-1:
                print("The first", m,"prime numbers are : ")
                print()
                for i in list:
                    print(i)                    
                break
                
                
                        
