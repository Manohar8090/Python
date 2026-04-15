#program for generating 1 to N Mul Tables where N is +VE
#InnerLoopsEx6.py
fromtab=int(input("Enter From where u want Mul tables:"))
uptotab=int(input("Enter up to where u want Mul tables:"))
if(fromtab<=0) or (uptotab<=0):
    print("Invalid Input")
else:
    if(fromtab<uptotab):
        for num in range(fromtab,uptotab+1):# This Loop supply the Number
            print("-" * 50)
            print("Mul Table for:{}".format(num))
            print("-" * 50)
            for i in range(1, 11):  # generates mul table for the number supplied by outer loop
                print("\t{} x {} = {}".format(num, i, num * i))
            print("-" * 50)
    else:
        if (fromtab > uptotab):
            for num in range(fromtab, uptotab-1,-1):  # This Loop supply the Number
                print("-" * 50)
                print("Mul Table for:{}".format(num))
                print("-" * 50)
                for i in range(1, 11):  # generates mul table for the number supplied by outer loop
                    print("\t{} x {} = {}".format(num, i, num * i))
                print("-" * 50)
        else:
            num=fromtab #OR num=uptotab
            print("-" * 50)
            print("Mul Table for:{}".format(num))
            print("-" * 50)
            for i in range(1, 11):  # generates mul table for the number supplied by outer loop
                print("\t{} x {} = {}".format(num, i, num * i))
            print("-" * 50)



