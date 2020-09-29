#To read a string: Calculate and print Total no of digits, alphabets, spaces and other characters
s=input("Enter a string : ")
uc=lc=sp=no=other=0
for a in range(len(s)):
    if (s[a]>='a' and s[a]<='z'):
        lc+=1
    elif(s[a]>='A' and s[a]<='Z'):
        uc+=1
    elif(s[a]>='0' and s[a]<='9'):
        no+=1
    elif s[a]==' ':
        sp+=1        
    else :
        other+=1
        
print("Number of Upercase Letters is :",uc)
print("Number of Lowercase Letters is :",lc)
print("Total Number of Letters is :",uc+lc)
print("Number of Digits is :",no)
print("Number of Spaces is :",sp)
print("Number of Special Characters is :",other)
