r=int(input("Enter size:"))
for x in range(0,r+1):
    for j in range(0,x):
        print(" ",end='')
    for k in range(0,2*r+1):
        print("*",end='')
    r-=1
    print()
