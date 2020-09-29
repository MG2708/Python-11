#Print user entered word in 3 rows and 5 columns
n=str(input("Enter a WORD : "))
for i in range(3):
    for j in range(1,6):
        print(n, end='  ')
    print()
