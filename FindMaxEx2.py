#program for Finding Max Value from List of Numbers
# witht using pre-defined function max()
#FindMaxEx1.py
n=int(input("Enter How Many Numbers u have:"))#n=5
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
        print(lst) # lst=[10,2,30,4,50]
        print("--------------------------------")
        print("Max({})={}".format(lst,max(lst)))
        print("--------------------------------")

# n=int(input("Enter How many number u have:"))
# if(n<=0):
#     print("\t{} is valid input".format(n))
# else:
#     lst=[]
#     for i in range(1,n+1):
#         value=int(input("Enter {} Value:".format(i)))
#         lst.append(value)
#     else:
#         print("-"*40)
#         print("Lists of value")
#         print(lst)
#         print("-"*40)
#         print("max({})={}".format(lst,max(lst)))
#         print("-"*40)