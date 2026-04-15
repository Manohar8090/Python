#EmployeeUpdate.py<---Module Name
import pickle
def updateemployee():
    with  open("E:\\KVR-PYTHON-11AM\\FILES\\empproj.data", "rb") as fp:
        records=[]
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #accept employee number for Updating Other deatils
    found=False
    empno=int(input("Enter Employee Number for Updating Details:"))
    for index in range(len(records)):
        if records[index][0]==empno:
            found=True
            recindex=index
            break
    #Update the records if the empno found
    if found:
        empnewsal=float(input("Enter Employee New Salary:"))
        empcompname=input("Enter Employee New Company Name:")
        records[recindex][2]=empnewsal
        records[recindex][3]=empcompname
        #Place the records from main memory into the file of secondary memory
        with open("E:\\KVR-PYTHON-11AM\\FILES\\empproj.data", "wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("Employee Details Updated--verify")
    else:
        print("Employee Details Not Found")


