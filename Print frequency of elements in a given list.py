#Print frequency of elements in a given list and print list of unique and duplicate elements
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)

print("The given list is : ",a)
print("The frequencies of all the elements are as follows :")

x=[]
y=[]
length=len(a)
count=i=0
while i < length:
    m=a[i]
    count=1
    if m not in x and m not in y:
        i+=1
        for p in range(i,length):
            if m==a[p]:
                count+=1
        else:
            print("Element : ",m, "- Frequency::", count)
            
    else:
        i+=1
