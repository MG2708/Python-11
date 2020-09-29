#Determine if the entered character is in UPPERCASE, lowercase or is a numerical, space or special character
a=str(input("Enter a character:"))
if a >= 'A' and a<= 'Z' :
    print("The entered character is in UPPERCASE")
elif a >= 'a' and a<= 'z' :
    print("The entered character is in lowercase")
if a >= '0' and a<='9' :                 #As entered value is character not a number
        print(" The enterd character is in numerical form")
elif a== '  ':
        print("The entered character is SPACE character")
else :
        print("Entered character is a Special One...")
        
