n=10
m=65
for i in range(1,11):
    r=chr(m)
    for j in range(0,i):
        print(n,r,end='%   ')
    m+=1
    n-=1
    print()
