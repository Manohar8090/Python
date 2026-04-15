#Program for generating list of Prime Numbers within range N
#InnerLoopsEx8.py
nopr=int(input("Enter the Range in which u want Primes:"))
if(nopr<=1):
    print("\t{} is Invalid Input".format(nopr))
else:
    print("-"*40)
    print("List of Primes within {}".format(nopr))
    print("-" * 40)
    for num in range(2,nopr+1): # Supply the Number
        res=True
        for i in range(2,num):#decides the whether the Outer for loop supplied number is prime or not
            if num % i == 0:
                res=False
                break
        if(res):
            print("\t{}".format(num))
    print("-" * 40)

