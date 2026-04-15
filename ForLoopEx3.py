#program for Generating  all even numbers within in N where N is +VE
#ForLoopEx3.py
n=int(input("Enter How Many Even Numbers Within the Range:"))#5
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("EVen Numbers within:{}".format(n))
    print("-" * 50)
    for i in range(2,n+1,2):
        print("\t{}".format(i))
    else:
        print("-" * 50)

