#Input sentences until enter key is pressed twice then print all the sentences in uppercase and lowercase
print("Enter a line in mixed case and press enter to print other ! Press enter twice to terminate and get result !!")
lines=[]
lines2=[]
while True:
    l=input()
    if l:
        lines.append(l.upper())
        lines2.append(l.lower())
    else:
        break
print()    
print("Entered lines in uppercase are: ")
for l in lines:
    print(l)
print()
print("Entered lines in lowercase are: ")
for l in lines2:
    print(l)



