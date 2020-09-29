#Sum of Factorials of 1 to 5
def fact(n):
   if n==1:
      return n
   else:
      return n * fact(n-1)

print("sum of Factorials of 1 to 5 is:")
print(fact(1)+fact(2)+fact(3)+fact(4)+fact(5))
print("Where:")
for i in range(1,6):
    print("Factorial of", i,"is",fact(i))
