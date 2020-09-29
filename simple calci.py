# Perepare a simple calculator using if - else condition to perform simple arithmetic functions (add, subtracrt , multiply, divide, and to get remainder) for entered two values
a=float(input("Enter a number "))
b=float(input("Enter second number with which to perform the simple arithmetic operations"))
c=input("Choose a operator [ + , - , / , *, %[To get remainder when a is divided by b ] ")
if c == '+' :
    print("The addition of two entered numbers is : " , a+b)
elif c=='-' :
     print("The subtraction of two entered numbers is : " , a-b)
if c == '*' :
    print("The multiplication of two entered numbers is : " , a*b)
elif c=='/' :
     print("The division of two entered numbers is : " , a / b)
if c=='%' :
    print("The remainder when a is divided by b is:" , a%b)
else:
    print("You need to get admission in Grade 1 and learn the basic mathematical operators... Entered Operator is INVALID !!!")
    
     
    
