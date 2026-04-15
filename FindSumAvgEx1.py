#program for Finding sum and average of List of Numbers
# without using pre-defined function sum()
#FindSumAvgEx1.py
n=int(input("Enter How Many Numbers Sum and average u want to find:"))#n=5
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    lst=[] # create empty list
    for i in range(1,n+1):
        value=float(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("--------------------------------")
        print("List of Values")
        print(lst) # lst=[10,20,30,40,50]
        print("--------------------------------")
        #Code for Finding Sum of List of Values
        s=0
        for val in lst:
            s+=val
        else:
            print("Sum={}".format(s))
            print("Avg={}".format(s/len(lst)))
            print("--------------------------------")
