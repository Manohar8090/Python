#program for accepting List of Values and Find sum and avg by using functions
#FunSumAvgEx2.py
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

def findsumvg():
    lst=readvalues() # One function Can Call another function-called function Chaining
    if(len(lst)==0):
        print("No Values Present in List-we can't compute Sum and Avg")
    else:
      print("\tGiven List Elements=",lst)
      print("\tSum=",sum(lst))
      print("\tAvg={}".format(sum(lst)/len(lst)))
#main Program
findsumvg()

