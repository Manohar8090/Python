#MulTableDemo.py<---Main Program
from MulExcept import NegativeNumberError,ZeroError,SpaceError
from builtins import ValueError
from MulTable import table
try:
    n=input("Enter a number for Gen Mul Table: ")
    table(n) # Function Call gives either Result or Excetions
except NegativeNumberError:
    print("\tDON'T ENTER -VE NUMBER TO MUL TABLE")
except ZeroError:
    print("\tDON'T ENTER ZERO TO MUL TABLE")
except ValueError:
    print("\tDon't enter alnums,strs and symbols for Mul Table")
except SpaceError:
    print("\tDon't Space for Mul table")
