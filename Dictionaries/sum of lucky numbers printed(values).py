#Random number between 21 to 50
#Key=Name of person
#Value=random number
#Record of lucky numbers(random no) upto n
#Sum of Lucky Numbers
import random
import json
n=int(input("Enter number of records to be made:"))
sum=0
for i in range(n):
    m=input("Enter name:")
    p=random.randint(21,50)
    d={"NAME":m,"LUCKY NUMBER":p}
    print(json.dumps(d,indent=0))
    print()
    num=d.get("LUCKY NUMBER")
    sum=sum+num
print("SUM OF ALL LUCKY NUMBERS PRINTED IS:",sum)



