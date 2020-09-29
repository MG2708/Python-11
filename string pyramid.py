#Print characters of entered string in pyramid
r=str(input("Enter string:"))
a=len(r)
c=1
for i in range(0,a):
    for j in range(0,c):
        print(r[0:c],end=' ')
        c+=1
        print()
        break
       
