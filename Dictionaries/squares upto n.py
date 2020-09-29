#Squares of numbers upto n
n=int(input("Enter upper range :"))
sq={}
for i in range(1,n+1):
    key=i
    value=i*i
    sq[key]=value
print("The dictionary is :")
print(sq)
