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
        print(lst) # lst=[10,2,30,4,50]
        print("--------------------------------")
        #Code for finding Max
        maxval=lst[0] # maxval=10
        for val in lst:
            if val>maxval:
                maxval=val
        else:
            print("Max({})={}".format(lst,maxval))
            print("--------------------------------")


# n=int(input("Enter How many number u Have:")) #n=5
# if(n<=0):
#     print("\t{} is invalid input".format(n))
# else:
#     lst=[] # create empty list
#     for i in range(1, n+1):
#         value=float(input("Enter {} Value:".format(i)))
#         lst.append(value)
#     else:
#         print("-"*40)
#         print("List of Values")
#         print(lst) # lst=[10,2,30,13,4,50]
#         print("-"*40)
#         # Code for finding Max 
#         maxval=lst[0] # maxval=10
#         for val in lst:
#             if val>maxval:
#                 maxval=val
#         else:
#             print("Max({})={}".format(lst,maxval))
#             print("-"*40)


# n=int(input("Enter how many number u are given"))
# if(n<=0):
#     print("\t{} is valid input".format(n))
# else:
#     lst=[] # create empty list
#     for i in range(1, n+1):
#         value=int(input("Enter {} value:".format(i)))
#         lst.append(value)
#     else:
#         print("-"*40)
#         print("lists of values")
#         print(lst)
#         print("-"*40)
#     # code find a max value
#     maxval=lst[0]
#     for val in lst:
#         if val>maxval:
#             maxval=val
#     else:
#         print("max({})={}".format(lst,maxval))
#         print("-"*40)