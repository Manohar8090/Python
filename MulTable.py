#MulTable.py<---File Name and module name
from MulExcept import ZeroError, NegativeNumberError, SpaceError
def table(n):
    if n.isspace():
        raise SpaceError
    else:
        num=int(n) # there is a Possitibility of raising ValueError
        if num==0:
            raise ZeroError
        elif num<0:
            raise NegativeNumberError
        else:
            print("-"*50)
            print("\tMul table for:{}".format(num))
            print("-" * 50)
            for i in range(1,11):
                print("\t{} x {} = {}".format(num,i,num*i))
            print("-" * 50)