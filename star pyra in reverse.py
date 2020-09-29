n=int(input("Enter the number of rows needed"))
for i in range(0,n):
    for j in range(n, i, -1):
        print("* ", end="")
    print()
