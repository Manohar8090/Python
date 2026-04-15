#DivOperationDemo.py<---main program
from DivExcept import DenDivsionError
from DivOperation import division
while(True):
    try:
        a = float(input("\tEnter First number:"))
        b = float(input("\tEnter Second number:"))
        res=division(a,b) # function call--gives either result or exception
    except DenDivsionError:
        print("\tDon't enter Zero for Denominator")
    except ValueError:
        print("\tDon't enter alnums,strs and symbols")
    else:
        print("\tDiv({},{})={}".format(a,b,res))
        break