#List in ascending order
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
    
print("The entered list is : ", a)    
m=[]
while a:
    minv=a[0]
    for p in a:
        if p< minv:
            minv=p
    a.remove(minv)
    m.append(minv)

print("The entered list in ascending order is : ", m)
