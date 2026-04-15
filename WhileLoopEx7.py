#programming for Calculating sum of First N Natural Numbers
#whileLoopEx7.py
n=int(input("Enter How Many Natural Number Sum u want:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("-"*50)
    print("First {} Natural Numbers".format(n))
    print("-" * 50)
    p=0 # Additive Identity.
    i=1
    while(i<=n):
        print("\t{}".format(i))
        p=p+i
        i=i+1
    else:
        print("-" * 50)
        print("Sum={}".format(p))
        print("-" * 50)