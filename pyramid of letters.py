#Pyramid of letters
r=int(input("Enter size:"))
A=65
for i in range(0,r):
    for j in range(i+1):
        print(chr(A),end='')
        A+=1
    print()
    
