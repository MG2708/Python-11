#Print a list arranged in ascending order with inserting a new element at perfect location in middle of the list
m=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,m):
    elem=int(input("Enter element in ascending order: "))
    a.append(elem)
print("You entered the list ",a)

n=0
p=list(a)
g=int(input("Enter a number less than the last number of the entered list:"))
while n<len(a):
    if a[n]<g<a[n+1]:
        p.insert(n+1,g)
    n+=1

print("The updated list is ",p)
        
    
