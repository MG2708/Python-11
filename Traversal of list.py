# In a list update it with odd numbers multiplied by 2 and even multiplied by 5
# Traversal of List
m=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,m):
    elem=int(input("Enter element: "))
    a.append(elem)
b=[]
for g in range(0, len(a)):
    if a[g]%2==0:
        b.append((a[g])*5)
    else:
        b.append((a[g])*2)
    g+=1

print("The given list is ", a)
print("The updated list is ", b)
    
