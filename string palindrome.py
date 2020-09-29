#String palindrome
print("Be Careful !! The program is case sensitive !!")
r=str(input("Enter string : "))
a=len(r)
b=a//2
last=-1
for c in range(b):
    if r[c]==r[last]:
        c+=1
        last-=1
    else:
        print("Entered string",r,"is not a palindrome")
        break
else:
    print("Entered string",r,"is a palindrome")
