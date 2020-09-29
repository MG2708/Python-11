#Find the max and min value from the entered list with index
m=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,m):
    elem=int(input("Enter element: "))
    a.append(elem)
l=len(a)
minv=a[0]
maxv=a[0]
for g in range(1,l):
    if a[g]<minv:
        minv=a[g]
    elif a[g]>maxv:
        maxv=a[g]

print("The entered list is :", a)
print("The minimum value is :", minv, "and is located at index : ",a.index(minv))
print("The maximum value is :", maxv, "and is located at index : ",a.index(maxv))
