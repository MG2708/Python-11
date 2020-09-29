#Print pyramid of stars for user entered number of rows
n=int(input("Enter the number of rows : "))
for i in range(0,n):
    for j in range(3,i+4):
        print('*',end=' ')
    print()
