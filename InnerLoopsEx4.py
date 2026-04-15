#Program for Demonstrating the Functionality of inner Loops
#InnerLoopsEx4.py
for i in range(1,6): #Outer loop
    print("*"*50)
    print("Outer loop:Value of i={}".format(i))
    print("*" * 50)
    j=3
    while(j>=1):#Inner loop
        print("\tInner loop:Value of j={}".format(j))
        j=j-1
    else:
        print("\tI am out-off Inner loop-else part:")
        print("-" * 50)
else:
    print("\tI am out-off Outer loop-else part:")
    print("*" * 50)