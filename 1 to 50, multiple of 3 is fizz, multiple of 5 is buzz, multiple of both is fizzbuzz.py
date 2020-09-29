#1 to 50
#multiple of 3 = Fizz
#multiple of 5 = Buzz
# multiple of both = FizzBuzz
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i %3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        
    
    
    
