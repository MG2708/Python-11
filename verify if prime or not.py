#Verify if entered no is prime or not

num=int(input("Enter a number : "))

for i in range(2,num):
    if (num % i) == 0:
        print(num,"is not a prime number")
        break
else:
    if num==1:
        print("1 is neither a prime nor a composite number !")
    else:
        print(num,"is a prime number")
               
