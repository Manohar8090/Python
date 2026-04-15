#program for Reading List of Values and Display
#ReadValuesEx1.py
n=int(input("Enter How Many Numbers u Have:"))#n=5
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    lst=[] # create empty list
    for i in range(1,n+1):
        value=float(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("List of Values")
        print(lst)