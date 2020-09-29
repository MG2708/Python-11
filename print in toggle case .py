#Print in Toggle Case
s=input("Enter a string : ")
s2=''
for a in range(len(s)):
    if (s[a]>='a' and s[a]<='z'):
        s2=s2+chr((ord(s[a])-32))
    elif(s[a]>='A' and s[a]<='Z'):
        s2=s2 + chr((ord(s[a])+32))
    else :
        s2=s2+s[a]
print(s2)

   
