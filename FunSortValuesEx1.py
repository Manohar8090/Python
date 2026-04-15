#Program for accepting List of Values and sort them in Ascending and Decending order
#FunSortValuesEx1.py
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
def sortvalues():
    lst=readvalues()
    if(len(lst) == 0):
        print("List is empty-can't sort the Data")
    else:
        print("Given Elements=",lst)
        lst.sort()
        print("Ascending Order=",lst)
        lst.sort(reverse=True)
        print("Decending Order=",lst)

#Main Program
sortvalues()
