#Dictionary for 3 family members then combine them into 1
#Details about name,age,hobby
#Father,Mother,Sibling
import json
fNAME=input("Enter Name of Father: ")
fage=int(input("Enter age: "))
fhobby=input("Enter hobby: ")
f={"NAME":fNAME,"AGE":fage,"HOBBY":fhobby}
print()
mNAME=input("Enter Name of Mother: ")
mage=int(input("Enter age: "))
mhobby=input("Enter hobby: ")
m={"NAME":mNAME,"AGE":mage,"HOBBY":mhobby}
print()
sNAME=input("Enter Name of Sibling: ")
sage=int(input("Enter age: "))
shobby=input("Enter hobby: ")
s={"NAME":sNAME,"AGE":sage,"HOBBY":shobby}
print()
print(f)
print(m)
print(s)
print()
myfamily={'FATHER':f,'MOTHER':m,'Sibling':s}
print(json.dumps(myfamily,indent=1))




