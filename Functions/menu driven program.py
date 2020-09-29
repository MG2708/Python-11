#Menu Driven Program
#1. Factorial
#2. Fibonacci Series
#3. Prime Numbers till n
#4. Binary Series
print("Menu Driven Program ")
def menu():
    print("Select which option to print : ")
    print('1. Factorial')
    print('2. Fibonacci Series')
    print('3. First N Prime Numbers')
    print('4. Binary Series')
    print('5. Exit')

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
                    print()
                    for i in list:
                        print(i)                    
                    break

#Binary Series
def binary(n):
    for i in range(n):
        print(2**i, end=' ' )
        
choice=1
while choice !=5:
    menu()
    choice=int(input("Select Option Number :"))
    n=int(input("Enter N :"))
    if choice==1:
        print(fact(n))
    elif choice==2:
        fibo(n)
    elif choice==3:
        prime(n)
    elif choice==4:
        binary(n)
    else:
        exit()
print("Thank You")
    
