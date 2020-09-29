#Create A Dynamic List
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=eval(input("Enter element: "))
    a.append(elem)
print(a)
