#program for generating All Even Numbers in reverse order within the range
#ForLoopEx6.py
n=int(input("Enter the Range in which odd Numbers u want generate:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    if(n%2==0):
        n=n-1
    for i in range(n,0,-2):
        print("\t{}".format(i))
    else:
        print("-"*50)
