#program for Generating 1 to N Numbers where N is +ve
#ForLoopEx1.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-" * 50)
    print("\tNumbers within :{}".format(n))
    print("-" * 50)
    for i in range(1,n+1):
        print("\t{}".format(i))
    else:
        print("-" * 50)

