#Updating a dictionary
#Dictionary D1 with name, age and basic salary
#Dictionary D2 with name and designation
name=input("Enter name :")
age=int(input("Enter age :"))
bs=int(input("Enter basic salary :"))
print()
name2=input("Enter name :")
desig=input("Enter designation :")
d1={"Name":name,"Age":age,"Basic Salary":bs}
d2={"Name":name2,"Designation":desig}
d1.update(d2)
print(d1)

