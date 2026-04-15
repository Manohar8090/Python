#program for accepting List of Values and Find sum and avg by using functions
#FunSumAvgEx1.py
def readvalues():
    n = int(input("Enter How Many Numbers u Have:"))  # n=5
    if (n <= 0):
        return [] # returning empty list
    else:
        lst = []  # create empty list
        for i in range(1, n + 1):
            value = float(input("Enter {} Value:".format(i)))
            lst.append(value)
        return lst

def findsumvg(lst): # lst=[]
    if(len(lst)==0):
        print("No Values Present in List-we can't compute Sum and Avg")
    else: # lst[10,20,30,40]
        s=0
        for val in lst:
            s=s+val
        else:
            print("\tGiven List Elements=",lst)
            print("\tSum=",s)
            print("\tAvg={}".format(s/len(lst)))
#main Program
lst=readvalues()
findsumvg(lst)

