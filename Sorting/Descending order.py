#Print in descending order(Using Bubble Sorting)
n=int(input("Enter number of elements: "))
a=[]
ctr=0
for i in range(n):
    elem=int(input("Enter element: "))
    a.append(elem)
print("The list created in descending order is :")
for i in range(len(a)-1,-1,-1):
    for j in range(i):
        if a[j] < a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            ctr+=1
    print(a)
print("The number of iterations are :",ctr)
