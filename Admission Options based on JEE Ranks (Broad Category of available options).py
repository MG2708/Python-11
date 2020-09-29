#Admission Options based on JEE Ranks (Broad Category of available options)
m=input("Enter your name :")
g=int(input("Enter your JEE AIR (for Advance) : "))
if g<=1000:
    print("Great Efforts",m ," ! You may choose any of the IIT/Top 10 ranked Govt College/Top 10 ranked Private College or any college of your choice :)")
elif g>1000 and g<=2000:
    print("Good Efforts",m," ! You may choose any of the NIT/Second Level Govt College/Second Level Private College :) ")
elif g>2000 and g<=10000:
    print("Nice Efforts",m," ! You may choose any of the Private College,But, Don't think of Top ones :) ")
elif g>10000 :
    print("Admissions Closed !! More Efforts Needed",m," ! Try Again ! Better Luck Next TIme OR Think to change your Career Option :) ")

