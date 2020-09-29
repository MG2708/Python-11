n=int(input("Enter the number of rows you want: "))
k = (2*n) - 2
m=65
for i in range(0,n):
    for j in range(0,k):
        print(end=" ") 
    k = k - 1
    for j in range(0, i+1):
        print(chr(m) , end=" ")
        m=m+1
    print()
    
  
