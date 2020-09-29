#Sum of all values of dicctionary
#Total no of awards won
sum=0
n=int(input("Enter number of students: "))
win={}
for i in range(n):
    key=input("Enter name : ")
    value=int(input("Enter number of awards won : "))
    win[key]=value
    sum+=value
print("The dictionary created is : ")
print(win)
print("Total number of awards won :",sum)

