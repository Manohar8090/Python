#program for Generating Mul Table for a Given Number where n is +ve
#ForLoopEx7.py
n=int(input("Enter a Number for Generating Mul Table:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("-" * 50)
    print("Mul table for:{}".format(n))
    print("-" * 50)
    for i in range(1,11):
        print("\t{} x {} = {}".format(n,i,n*i))
    else:
        print("-" * 50)
print("-" * 50)
print("By using While loop")
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("-" * 50)
    print("Mul table for:{}".format(n))
    print("-" * 50)
    i=1
    while(i<=10):
        print("\t{} x {} = {}".format(n,i,n*i))
        i+=1
    else:
        print("-" * 50)
