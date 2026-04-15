#programming for Calculating Factorial of Given +VE Number
#ForLoopEx11.py
n=int(input("Enter Number for Cal Fcatorial:"))
if(n<0):
    print("{} is invalid Input".format(n))
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    else:
        print("Factorial({})={}".format(n,fact))


