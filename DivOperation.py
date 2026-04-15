#DivOperation.py<---File Name and Module Name
from DivExcept import DenDivsionError
def division(a,b):
    if(b==0):
        raise DenDivsionError # Hiiting the programmer-Defined exception
    else:
        return a/b

#Phase-2: development of Business Logic by Hitting Programmer Defined Exception