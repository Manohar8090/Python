#program for Generating N to 1
#ForLoopEx2.py
n=int(input("Enter How Many Numbers u want to generate:"))#5
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("Numbers from {} to 1".format(n))
    print("-" * 50)
    for i in range(n,0,-1):
        print("\t{}".format(i))
    else:
        print("-" * 50)

