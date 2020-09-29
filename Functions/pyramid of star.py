#Pyramid of star
def star(n):
    for i in range(0,n):
        for j in range(3,i+4):
            print('*',end=' ')
        print()

n=int(input("Enter number of rows : "))
star(n)
