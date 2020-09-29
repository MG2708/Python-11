#Basics to nested for loop (3)
n=1
for i in range(1,11):
    for j in range(0,i):
        print(n*n, end='  ')
        n=n+1
    print()
