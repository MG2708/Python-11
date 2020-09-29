#Print entered three numbers in ascending order
a=int(input("Enter a number         : "))
b=int(input("Enter another number   : "))
c=int(input("Enter the third number : "))
if a>b>c :
    print("The entered numbers in ascending order are :",c, '<',b,'<',a)
elif b>a>c :
    print("The entered numbers in ascending order are :",c, '<',a,'<',b)
elif c>a>b :
    print("The entered numbers in ascending order are :",b, '<',a,'<',c)
elif a>c>b :
    print("The entered numbers in ascending order are :",b, '<',c,'<',a)
elif b>c>a :
    print("The entered numbers in ascending order are :",a, '<',c,'<',b)
elif c>b>a :
    print("The entered numbers in ascending order are :",a, '<',b,'<',c)
elif b>a==c or b>c==a:
    print("The entered numbers in ascending order are :",c, '=',a,'<',b)
elif b==a>c or a==b>c:
    print("The entered numbers in ascending order are :",c, '<',a,'=',b)
elif a>b==c or a>c==b :
    print("The entered numbers in ascending order are :",c, '=',b,'<',a)
elif c>a==b or c>b==a :
    print("The entered numbers in ascending order are :",b, '=',a,'<',c)
elif a>c==b or a>b==c:
    print("The entered numbers in ascending order are :",b, '=',c,'<',a)
elif a==c>b or c==a>b :
    print("The entered numbers in ascending order are :",b, '<',a,'=',c)
elif b==c>a or c==b>a :
    print("The entered numbers in ascending order are :",c, '=',a,'<',b)
else:
    print("All the entered numbers are equal :",a, "=", b, '=', c)

