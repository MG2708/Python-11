#Print the fibonacci series for user entered value starting with 1,1 already
n=int(input("Enter the number of values to print : "))
ctr=ltop = l =1
lst=[1,1]
while ctr<=(n-2):
    c = ltop+l
    lst.append(c)
    ltop=l
    l=c
    ctr+=1
print(lst)
    
