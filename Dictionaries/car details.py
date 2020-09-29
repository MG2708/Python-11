#Dict car with details of brand,model,year
brand=input("Enter brand of your car: ")
model=eval(input("Enter Model: "))
year=int(input("Enter model year: "))
car={"BRAND":brand,"MODEL":model,"YEAR":year}
print(car)
print()
colour=input("Enter colour: ")
car['COLOUR']=colour
print(car)
print()
car.pop('YEAR')
print(car)
print()
newcar=car.copy()
print("NEW DICTIONARY USING COPY FUNCTION:")
print(newcar)
