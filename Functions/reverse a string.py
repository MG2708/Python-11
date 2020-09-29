#Reverse a string
def rev(x):
    temp=" "
    for i in x:
        temp=i+temp
    print(temp)
n=input("Enter a string :")
rev(n)
