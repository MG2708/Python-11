#Printing pyramid of letters followed by # and the square of the corresponding natural no for user entered number of rows
n=int(input("Enter the number of rows :"))
m=1
p=65
for i in range(1,n+1):
    for j in range(0,i):
        g=chr(p)
        print(g,end='#'),
        print( m*m, end=' ' )
        m+=1
        p+=1
    print()
