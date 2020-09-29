#Program to Reverse a Number    
m = int(input("Please Enter any Number: "))    
n= 0    
while(m> 0):    
    p= m %10    
    n = (n*10) +p  
    m = m //10    
     
print("\n Reverse of entered number is =", n) 
