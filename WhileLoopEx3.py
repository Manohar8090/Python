#program for Generating N to 1
#WhileLoopEx3.py
n=int(input("Enter How Many Numbers u want to generate:"))#5
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("Numbers from {} to 1".format(n))
    print("-" * 50)
    i=n # Init Part
    while(i>=1):
        print("\t{}".format(i))
        i=i-1 # OR i-=1
    else:
        print("-" * 50)


