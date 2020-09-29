#Bill Of A General Provision Store
n1=input('Enter the name of the product purchased:')
p1=float(input('Enter the price per piece of the product;'))
q1=int(input('Enter the quantity of the product purchased:'))
n2=input('Enter the name of the product purchased:')
p2=float(input('Enter the price per piece of the product;'))
q2=int(input('Enter the quantity of the product purchased:'))
n3=input('Enter the name of the product purchased:')
p3=float(input('Enter the price per piece of the product;'))
q3=int(input('Enter the quantity of the product purchased:'))
t1=(q1*p1)
t2=(q2*p2)
t3=(q3*p3)
T=((t1+t2+t3)*18) /100
print('\t\t\t    All In One General Store')
print('--------------------------------------------CASH MEMO--------------------------------------------')
print('\nPRODUCT \t   \t PRICE  \t \t   QUANTITY  \t\tTOTAL')
print(n1,' \t\t\t', ' ',p1,' \t\t' ,'     ',q1, '\t\t\t', t1)
print(n2 ,'\t\t\t', ' ',p2 ,'\t\t', '     ',q2,  '\t\t\t', t2)
print(n3,' \t\t\t', ' ',p3, '\t\t', '     ',q3, '\t\t\t' , t3 )
print('\n TAX APPLICABLE = ' , T)
print('\n \t\t\t\t\t\t  Net Total =', t1+t2+t3+T)



