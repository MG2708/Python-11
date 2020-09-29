#Nested Dictionary with Marks of phy and chem of two Students
#Using items function
name=input("Enter Name:")
phy=float(input("Enter marks in Physics:"))
chem=float(input("Enter marks in Chemistry:"))
print()
name2=input("Enter Name:")
phy2=float(input("Enter marks in Physics:"))
chem2=float(input("Enter marks in Chemistry:"))
st1={"NAME":name,"PHYSICS":phy,"CHEMISTRY":chem}
st2={"NAME":name2,"PHYSICS":phy2,"CHEMISTRY":chem2}
d={"Record1":st1,"Record2":st2}
import json
print(json.dumps(st1,indent=0))
print()
print(json.dumps(st2,indent=0))
print()
newdict=d.items()
print(newdict)



