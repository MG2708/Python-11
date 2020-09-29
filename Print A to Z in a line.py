#program to print the English Alphabet in a single line
for x in range(65,91):
    letter = chr(x)
    alphabet = " " + letter
    print (alphabet, end='  ')
