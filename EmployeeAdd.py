#EmployeeAdd.py<---Module Name
import pickle
import sys
sys.path.append("E:\\KVR-PYTHON-11AM\\EXCEPTIONS\\CASE-3")
from NameValidation import validatename
from NameExcept import ZeroNameLengthError, SpaceError,InValidNameError

def isunique(lst): # lst=[600,"KV",0.0,"NIT"]
    with open("E:\\KVR-PYTHON-11AM\\FILES\\empproj.data", "rb") as fp:
        records=[]
        while(True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        found=True
        for record in records:
            if (record[0]==lst[0]):
                found=False
                break

        return found

def addemployee():
    with open("E:\\KVR-PYTHON-11AM\\FILES\\empproj.data", "ab") as fp:
        while (True):
            try:
                print("-" * 50)
                empno = int(input("\tEnter Employee Number:"))
                name = input("\tEnter Employee Name:")
                empname=validatename(name)
                empsal = float(input("\tEnter Employee Salary:"))
                comp= input("\tEnter Employee Company Name:")
                empcomp=validatename(comp)
                print("-" * 50)
                lst = list()  # Create empty list for adding employee values
                # append emp values to lst object
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                lst.append(empcomp)
                # Save the Iterable object content to the file
                if(isunique(lst)):
                    pickle.dump(lst, fp)
                    print("\tEmployee Data Saved as Record in File Sucessfully")
                else:
                    print("\tEmployee Number alerady exist-try with Unique Emp Number")
                print("-" * 50)
                ch = input("\tDo u want to enter another employee details(yes/no):")
                if (ch.lower() == "no"):
                    break
                print("-" * 50)
            except ValueError:
                print("\tDon't enter alnums,strs and symbols for empno andd salary")
            except SpaceError:
                print("\tDON'T ENTER SPACE FOR UR NAME-Try Again")
            except ZeroNameLengthError:
                print("\tENTER FOR UR NAME-Try Again")
            except InValidNameError:
                print("\tInvalid Emp Name/ Comp Name-Try again")
