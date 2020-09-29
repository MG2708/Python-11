#Print binary series till n where n is the user entered value
n=int(input('Enter a number : '))
for i in range(0,n+1):
    print(2**i ,end='   ') 
