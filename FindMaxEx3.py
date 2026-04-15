#program for Finding Max Value from List of Numbers
# without using pre-defined function max()
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
        print(lst) # lst=[10,20,3,4,50]
        print("--------------------------------")
        #Code for finding Max
        maxval=lst[0] # maxval=10
        for index in range(1,len(lst)):
            if lst[index]>maxval:
                maxval=lst[index]
        else:
            print("Max({})={}".format(lst,maxval))
            print("--------------------------------")

# n=int(input("Enter how many number u have:"))
# if(n<=0):
#     print("\t{} is invalid input".format(n))
# else:
#     lst=[]
#     for i in range(1, n+1):
#         value=int(input("Enter {} Value:".format(i)))
#         lst.append(value)
#     else:
#         print("-"*40)
#         print("Lists of values")
#         print(lst)
#         print("-"*40)
#         #code for finding max
#         maxval=lst[0]
#         for index in range(1,len(lst)):
#             if lst[index]>maxval:
#                 maxval=lst[index]
#         else:
#             print("Max({})={}".format(lst,maxval))
#             print("-"*40)

    