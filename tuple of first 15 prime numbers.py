lst=[]
ctr=1
while ctr<=15:
    for val in range(100):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                lst.append(val)
                ctr+=1
                if ctr > 15:
                    break
                
print("The tuple with first 15 prime numbers is : ")
tup=tuple(lst)
print(tup)
              
                
                        
