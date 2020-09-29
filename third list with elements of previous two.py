m=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,m):
    elem=int(input("Enter element: "))
    a.append(elem)

n=int(input("Enter the number of elements to be inserted: "))
b=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    b.append(elem)
    
p=list(a)
p=p.extend(b)

print("First entered list is : ", a)
print("Second entered list is : ", b)
print("Updated list is : ", p)
