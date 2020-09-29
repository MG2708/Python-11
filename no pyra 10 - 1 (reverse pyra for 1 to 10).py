#Basics to nested for loop (5)
n=10
for i in range(1,5):
    for j in range(0,i):
        print(n, end='  ')
        n=n-1
    print()
