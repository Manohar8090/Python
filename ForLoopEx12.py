#programming for Calculating Factorial of Given +VE Number
#ForLoopEx12.py
n=int(input("Enter Number for Cal Fcatorial:"))
if(n<0):
    print("{} is invalid Input".format(n))
else:
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    else:
        print("\t{}!={}".format(n,fact))


