#Reverse pyramid 5 to 1
n=5
for i in range (1,6):
    for j in range(5,i-1,-1):
        print(n,end='')
    n-=1
    print()
