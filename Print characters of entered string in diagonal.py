#Print characters of entered string in diagonal
r=str(input("Enter string:"))
b=0
for a in r:
    for i in range(0,b):
        print(" ",end='')
    b+=1
    for j in range(0,1):
        print(a,end='')
    print()
