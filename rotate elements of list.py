#Rotate elements of a list
a=list(eval(input("Enter list:" )))
l=len(a)
b=[]
b.append(a[-1])
for i in range(0,l-1):
    b.append(a[i])
print("The original list is :")
print(a)
print()
print("The new list is :")
print(b)
