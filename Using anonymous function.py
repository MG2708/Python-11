#Using anonymous function
terms=10
result=list(map(lambda x:2**x,range(terms)))
print("The total terms is:",terms)
for i in range(terms):
    print("2 ",i,"is",result[i])
