#NameValidationDemo.py<--Main Program
from NameValidation import validatename
from NameExcept import ZeroNameLengthError, SpaceError,InValidNameError
while(True):
    try:
        name=input("Enter Ur Name:")
        validname=validatename(name) # Function Call give either Valid Name Or exceptions
    except SpaceError:
        print("\tDON'T ENTER SPACE FOR UR NAME-Try Again")
    except ZeroNameLengthError:
        print("\tENTER FOR UR NAME-Try Again")
    except InValidNameError:
        print("\t{} Is Invalid Name-Try again".format(name))
    except:
        print("\tOooopps Some thing went wrong--try agin")
    else:
        print("\tUR NAME:{}".format(validname))
        break