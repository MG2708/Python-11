#Insertion Sort
n=int(input("Enter number of elements: "))
lst=[]
ctr=0
for i in range(n):
    elem=int(input("Enter element: "))
    lst.append(elem)
print("The list created after insertion sorting is :")
for i in range(1,len(lst)):
    a=lst[i]
    j=i-1
    while j>=0 and a<lst[j]:
        lst[j+1]=lst[j]
        j=j-1
    else:
        lst[j+1]=a
        ctr+=1
    print(lst)
print("The total number of iterations are :",ctr)
