n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=eval(input("Enter element: "))
    a.append(elem)

m=int(input("Enter the number of elements to be inserted: "))
b=[]
for i in range(0,m):
    elem=eval(input("Enter element: "))
    b.append(elem)

c=list(a)
for p in b:
    c.append(p)

print("The first entered list is :", a)
print("The second entered list is :", b)
print("The third list with elements of previous two lists is :", c)
