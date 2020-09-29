#Print letters of entered string in reverse pyra
r=str(input("Enter string:"))
a=len(r)
for i in range(0,a):
    for j in range(0,a):
        print(r[0:a],end='')
        a-=1
        print()
