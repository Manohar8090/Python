#Program for Finding GCD and LCM of Two Given Integer Values
#GCDLCMEx.py
a=int(input("Enter First Integer Value:"))
b=int(input("Enter Second Integer Value:"))
if(a<0) or (b<0):
    print("Invalid Input")
else:
    oa=a
    ob=b
    #code for getting GCD
    while("KVR"):
        r=a%b
        if(r==0):
            gcd=b
            break
        a=b
        b=r
    print("\tGCD({},{})={}".format(oa,ob,gcd))
    print("\tLCM({},{})={}".format(oa,ob,(oa*ob)//gcd))
