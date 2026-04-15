#program for Generating 1 to N Numbers where N is +ve
#WhileLoopEx2.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-" * 50)
    print("\tNumbers within :{}".format(n))
    print("-" * 50)
    i=1 # Intilization Part
    while(i<=n): # Conditional Part
        print("\t{}".format(i))
        i+=1 # Updation Part--here += is called Short Hand + Operator
    else:
        print("-"*50)
