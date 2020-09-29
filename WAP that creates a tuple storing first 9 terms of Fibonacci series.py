#Tuple with first nine terms of fibonacci series
n=9
ctr=ltop = l =1
lst=[1,1]
while ctr<=(n-2):
    c = ltop+l
    lst.append(c)
    ltop=l
    l=c
    ctr+=1
t=tuple(lst)
print("Required tuple is :",t)
