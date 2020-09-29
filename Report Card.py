#For papers with maximum marks = 100
print("Please enter all the following marks out of 100")
sub1=float(input('Enter marks in first subject'))
sub2=float(input('Enter marks in second subject'))
sub3=float(input('Enter marks in third subject'))
sub4=float(input('Enter marks in fourth subject'))
sub5=float(input('Enter marks in fifth subject'))
gt=sub1+sub2+sub3+sub4+sub5
percent=(gt/500)*100
print('The grand total is:' , gt)
print("The percentage scored is:" , percent)
if percent>90:
    print("You scored excellent with grade A")
else:
    if percent>80:
        print("You scored good with grade B. Little effort is needed to excel !! ")
    else:
        if percent>70:
            print("You scored average with grade C. Need to work hard !! ")
        else:
            print("You have failed... :(  Padhai Chhod do Beta, Tumse na ho payega....")
                
    
                 
                 
