n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=eval(input("Enter element: "))
    a.append(elem)

m=eval(input("Element to be searched : "))
print("The entered list is :", a)
for p in a:
    if m==p:
        print("The element you had searched for is :",m, " and is located at index :",a.index(m))
        break
else:
    print("The element you searched for does not exist in the entered list!")
        
        
