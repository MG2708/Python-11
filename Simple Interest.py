#To print Simple Interest
P=float(input('Enter the Principle Amount'))
R=float(input('Enter the rate of interest'))
T=int(input('Enter the time period '))
SI=(P*R*T)/100
print('The interst is;', SI)
print('Amount after interest', P+SI)
