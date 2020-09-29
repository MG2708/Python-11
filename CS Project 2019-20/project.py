 #Menu Driven Program
#1. Factorial
#2. Fibonacci Series
#3. First N Prime Numbers
#4. Binary Series
#5. Prime Numbers till N
#6. Multiplication Table
#7. Reverse entered number
#8. Sum of digits of entered number
#9. Factors of N
#10. Exit

print("     Menu Driven Program")
def menu():
    print("Select which option to print : ")
    print('1. Factorial')
    print('2. Fibonacci Series')
    print('3. First N Prime Numbers')
    print('4. Binary Series')
    print('5. Prime Numbers till N')
    print('6. Multiplication Table')
    print('7. Reverse entered number')
    print('8. Sum of digits of entered number')
    print('9. Factors of N')
    print('10. Exit')
    
#factorial
def fact(n):
    f=1
    if n==0:
        return 1
    else:
        while n:
            f=f*n
            n-=1
        return f

#Fibonacci Series
def fibo(n):
    ctr=ltop = l =1
    lst=[1,1]
    while ctr<=(n-2):
        c = ltop+l
        lst.append(c)
        ltop=l
        l=c
        ctr+=1
    print(lst)

#First N prime numbers 
def prime(n):
    list=[]
    a=[]
    length=len(list)
    for val in range(1000000000):
        if val > 1:
            for m in range(2, val):
                if (val % m) == 0:
                    break
            else:
                list+=[val]
                length=len(list)
                if length > n-1:
                    print("The first", n,"prime numbers are : ")
                    for i in list:
                        print(i)                    
                    break

#Binary Series
def binary(n):
    for i in range(n):
        print(2**i, end=' ' )
        print()

#Prime Numbers till N
def primen(n):
    for i in range(0,n+1):
        if i>1:
            for j in range(2,i):
                if i%j==0 :
                    break
            else:
                print(i)

#Multiplication Table
def multi(n):
    for a in range(1,11):
        print(n, "X" , a, "=", a*n)

#Reverse the entered number
def rev(n):     
    m= 0    
    while(n> 0):    
        p= n %10    
        m = (m*10) +p  
        n = n //10    
    print("Reverse of entered number is =", m) 

#Sum of digits of entered number
def digsum(n):
    s=0
    while n!=0:
        g=n%10
        s=s+g
        n=int(n/10)
    ans=int(s)
    print("The sum of the digits of given number is : ",ans)

#Factors of N
def factor(n):
    print("The Factors of the number are:")
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
            
#Main Loop        
while(True):
    menu()
    print()
    choice=int(input("Select Option Number :"))
    if choice ==10:
        print("Thank You !")
        exit()
    else:
        n=int(input("Enter N :"))
        if choice==1:        
            print(fact(n))
            print()
        elif choice==2:
            fibo(n)
            print()
        elif choice==3:
            prime(n)
            print()
        elif choice==4:
            binary(n)
            print()
        elif choice==5:
            primen(n)
            print()
        elif choice==6:
            multi(n)
            print()
        elif choice==7:
            rev(n)
            print()
        elif choice==8:
            digsum(n)
            print()
        elif choice==9:
            factor(n)
            print()
      
    
