#program for Generating  all even numbers within in N where N is +VE
#WhileLoopEx4.py
n=int(input("Enter How Many Eeven Numbers Within the Range:"))#5
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("EVen Numbers within:{}".format(n))
    print("-" * 50)
    i=1
    while(i<=n):
        if(i%2==0):
            print("\t{}".format(i))
        i=i+1
    else:
        print("-" * 50)

