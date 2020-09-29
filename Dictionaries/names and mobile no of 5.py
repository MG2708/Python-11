#Nmaes and mobile number of 5
n=5
mob={}
for i in range(5):
    key=input("Enter name : ")
    value=int(input("Enter mobile number : "))
    mob[key]=value
print("The Dictionary created is :")
print(mob)
for j in mob:
    print(j,'is contact number of',mob[i])
