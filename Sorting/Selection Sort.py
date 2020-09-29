#Selection Sort
n=int(input("Enter number of elements: "))
a=[]
ctr=0
for i in range(n):
    elem=int(input("Enter element: "))
    a.append(elem)
print("Original list is :", a)
print()
print("The list created after selection sorting is :")
for i in range(len(a)):
    min_value=i
    for j in range(i+1,len(a)):
        if a[min_value] > a[j]:
            min_value=j
    a[i],a[min_value]=a[min_value],a[i]
    ctr+=1
    print(a)
print()
print("The number of iterations are :",ctr)
