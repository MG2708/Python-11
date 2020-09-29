#Second largest elememt of tuple
t=tuple(eval(input("Enter tuple: ")))
maxv=max(t)
l=len(t)
secmax=0
for a in range(l):
    if secmax<t[a]<maxv:
        secmax=t[a]
print("The second largest value is :",secmax)
