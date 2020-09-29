#Basics to nested for loop (8)
n=50
for i in range(1,5):
    for j in range(0,i):
        print(n, end='  ')
        n=n-5
    print()
