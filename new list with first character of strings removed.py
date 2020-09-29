n=int(input("Enter number of elements to be entered :"))
a=[]
for i in range(0,n):
    elem=input("Enter element :")
    a.append(elem)
print("The entered list is :",a)
for m in a:
    n=m[1:]
    a.append(n)
    
    
print("The updated list is :",a)
