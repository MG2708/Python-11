#squares of odd numbers in given range
n=int(input("Enter lower range :"))
m=int(input("Enter upper range :"))
p={}
for g in range(n,m+1):
    if g%2!=0:
        p[g]=g*g
print(p)
