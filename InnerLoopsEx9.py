#Program for generating list of Prime Numbers within range N
#InnerLoopsEx8.py
nopr=int(input("Enter the Range in which u want Primes:"))
if(nopr<=1):
    print("\t{} is Invalid Input".format(nopr))
else:
   plist=[]
   for num in range(2,nopr+1): # Supply the Number
        res=True
        for i in range(2,num):#decides the whether the Outer for loop supplied number is prime or not
            if num % i == 0:
                res=False
                break
        if(res):
            plist.append(num)
print("-" * 40)
print("List of Primes")
for x in plist:
    print(x)
print("-" * 40)

