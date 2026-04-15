#Program for Demonstrating the Functionality of inner Loops
#InnerLoopsEx3.py
i=5
while(i>=1): #Outer loop
    print("*"*50)
    print("Outer loop:Value of i={}".format(i))
    print("*" * 50)
    for j in range(3,0,-1):
        print("\tInner loop:Value of j={}".format(j))
    else:
        print("\tI am out-off Inner loop-else part:")
        i=i-1
        print("-" * 50)
else:
    print("\tI am out-off Outer loop-else part:")
    print("*" * 50)