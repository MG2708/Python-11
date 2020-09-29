#new list with first characters removed of elements of first list
n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    a=eval(input("Enter element :"))
    lst.append(a)
print()
lst2=[]
for a in lst:
    m=a[1:]
    lst2.append(m)

print("The original list is:")
print(lst)
print()
print("The new list created is :")
print(lst2)
    
