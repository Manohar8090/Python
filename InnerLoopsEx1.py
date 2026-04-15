#Program for Demonstrating the Functionality of inner Loops
#InnerLoopsEx1.py
for i in range(1,6): #Outer loop
    print("*"*50)
    print("Outer loop:Value of i={}".format(i))
    print("*" * 50)
    for j in range(1,4):#Inner loop
        print("\tInner loop:Value of j={}".format(j))
    else:
        print("\tI am out-off Inner loop-else part:")
        print("-" * 50)
else:
    print("\tI am out-off Outer loop-else part:")
    print("*" * 50)