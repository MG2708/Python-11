#Sum of squares of user entered values in a list
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem*elem)
sum=sum(a)
print("Sum of elements in the list" ,a ,"is",sum)
