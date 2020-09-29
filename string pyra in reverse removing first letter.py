r=str(input("Enter string:"))
a=len(r)
c=0
for i in range(0,a):
    for j in range(0,a):
        print(r[c:a],end=' ')
        c+=1
        print()
        break
