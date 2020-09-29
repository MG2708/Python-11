#Dictionary with awards won by sports winners
n=int(input("Enter number of students: "))
win={}
for i in range(n):
    key=input("Enter name : ")
    value=int(input("Enter number of awards won : "))
    win[key]=value
print("The dictionary created is : ")
print(win)
