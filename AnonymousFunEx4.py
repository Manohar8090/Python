#Program for accepting Two Numerical Values and
# Find Biggest among them
#AnonymousFunEx4.py
#Normal Fucntion
def kvrmax(lst): # lst=[10,20,3,40,5,-2,6,78,12]
    bigv=lst[0]
    for val in lst[1:]:
        if val>bigv:
            bigv=val
    return bigv

def kvrmin(lst):
    minv=lst[0]
    for val in lst[1:]:
        if val<minv:
            minv=val
    return minv

#Anonymous Functions
findmax=lambda lst: kvrmax(lst)
findmin=lambda lst: kvrmin(lst)

#Main Program
print("Enter List of Values separated by Comma:")
lst=[float(val) for val in input().split(",")]
if(len(set(lst))==1):
    print("All Values are Equal")
else:
    maxv=findmax(lst)
    minv=findmin(lst)
    print("Max={}".format(maxv))
    print("Min={}".format(minv))