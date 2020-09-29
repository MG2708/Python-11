#Print in Toggle Case and change numbers into @
s=input("Enter a string : ")
s2=''
for a in range(len(s)):
    if (s[a]>='a' and s[a]<='z'):
        s2=s2+chr((ord(s[a])-32))
    elif(s[a]>='A' and s[a]<='Z'):
        s2=s2 + chr((ord(s[a])+32))
    elif(s[a]>='0' and s[a]<='9'):
        s2=s2 + '@'
    else :
        s2=s2+s[a]
print(s2)

   
