#Sum of elements of List
def sum(a):
    total=0
    for i in a:
        total+=i
    print(total)
n=int(input("Enter number of elements : "))
a=[]
for i in range(n):
    elem=int(input("Enter element :"))
    a.append(elem)
print("Sum of elements of list is: ")
sum(a)
             
