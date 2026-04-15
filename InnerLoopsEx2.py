#Program for Demonstrating the Functionality of inner Loops
#InnerLoopsEx2.py
i=1
while(i<=5): #Outer loop
    print("*"*50)
    print("Outer loop:Value of i={}".format(i))
    print("*" * 50)
    j=1
    while(j<=3):#Inner loop
        print("\tInner loop:Value of j={}".format(j))
        j=j+1
    else:
        print("\tI am out-off Inner loop-else part:")
        i=i+1
        print("-" * 50)
else:
    print("\tI am out-off Outer loop-else part:")
    print("*" * 50)