#Second smallest element of list
a=eval(input("Enter list :"))
a=list(a)
print("Entered List is :",a)
minv=a[0]
sminv=a[1]
for i in a :
    if minv>i:
        minv=i
for j in a :
    if sminv>j and j!=minv:
        sminv=j
print("Smallest value of list is :",minv)
print("Second Smallest value of list is :",sminv)
