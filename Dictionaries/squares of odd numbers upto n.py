#squares of odd numbers upto n
n=int(input("Enter N :"))
sq={n:n*n for n in range(1,n+1,2)}
print(sq)
