#program for generating 1 to N Mul Tables where N is +VE
#InnerLoopsEx5.py
n=int(input("Enter How Many Mul Tables u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    for num in range(1,n+1):# This Loop supply the Number
        print("-"*50)
        print("Mul Table for:{}".format(num))
        print("-" * 50)
        for i in range(1,11):#generates mul table for the number supplied by outer loop
            print("\t{} x {} = {}".format(num,i,num*i))
        print("-" * 50)