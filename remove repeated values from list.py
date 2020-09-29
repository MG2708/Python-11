#Remove the repeated value from the user entered list
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=eval(input("Enter element: "))
    a.append(elem)

g=list(a)
m=0
while m <len(g):
    p=m+1
    while p < len(g):
        if g[m]==g[p]:
            del g[p]
            print("Value removed =",g[m]," from index =",p)
        else:
            p+=1
    m+=1                                     
print("The given list is : " ,a)
print("The updated list is : ", g)
