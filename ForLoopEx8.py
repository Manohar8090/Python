#programming for Calculating sum of First N Natural Numbers
#ForLoopEx8.py
n=int(input("Enter How Many Natural Number Sum u want:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("-"*50)
    print("First {} Natural Numbers".format(n))
    print("-" * 50)
    p=0 # Additive Identity.
    for i in range(1,n+1):
        print("\t{}".format(i))
        p=p+i
    else:
        print("-" * 50)
        print("Sum={}".format(p))
        print("-" * 50)