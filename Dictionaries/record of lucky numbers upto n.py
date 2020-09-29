#Random number between 21 to 50
#Key=Name of person
#Value=random number
#Record of lucky numbers(random no) upto n
import random
import json
n=int(input("Enter number of records to be made:"))
for i in range(n):
    m=input("Enter name:")
    p=random.randint(21,50)
    d={"NAME":m,"LUCKY NUMBER":p}
    print(json.dumps(d,indent=0))
    print()
    sum=sum+p
print("Sum of all the lucky numbers printed :",sum)


