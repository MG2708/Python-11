#Program to Check if entered year is Leap Year or not
year = int(input("Please Enter the Year Number you wish: "))

if(year%4 == 0)or(year%100 == 0)and(year%400 == 0):
    print("Entered year is a Leap Year",year)
else:
    print("Entered year is Not a Leap Year",year)
