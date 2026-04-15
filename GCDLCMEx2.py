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
    res=True
    while(res):
        r=a%b
        if(r==0):
            gcd=b
            res=False
        else:
            a=b
            b=r
    else:
        print("\tGCD({},{})={}".format(oa,ob,gcd))
        print("\tLCM({},{})={}".format(oa,ob,(oa*ob)//gcd))
