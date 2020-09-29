# To find the sum of the elements of a given list
n=int(input("Enter the number of elements to be inserted: "))
a=[]
s=0
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
    s=s+elem
print("The sum of elements of list is : ", s)


