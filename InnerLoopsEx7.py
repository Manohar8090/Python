#program for generating Mul Tables  List of +Ve Rabdom Numebrs
#InnerLoopsEx7.py
n=int(input("Enter How Many Mul Tables u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("\tEnter Number for Gen Mul table {}:".format(i)))
        lst.append(val)
    else:
        print("List of Random Numbers")
        print(lst) # [19, -12, 16, 0, 18]
        for num in lst: # get the num from list object
            if(num<=0):
                print("\t{} is invalid input".format(num))
            else:
                print("-"*50)
                print("Mul Table for:{}".format(num))
                print("-" * 50)
                for i in range(1,11):
                    print("\t{} x {} = {}".format(num,i,num*i))
                print("-" * 50)
