#Program for Reading the Emp details from Key Baord and save them as Record in File (emp.pick)
#EmpPickEx.py
import pickle
def saveempdata():
	with open("emp.pick","ab") as fp:
		while(True):
			print("-"*50)
			empno=int(input("Enter Employee Number:"))
			empname=input("Enter Employee Name:")
			empsal=float(input("Enter Employee Salary:"))
			print("-"*50)
			lst=list() # Create empty list for adding employee values
			#append emp values to lst object
			lst.append(empno)
			lst.append(empname)
			lst.append(empsal)
			#Save the Iterable object content to the file
			pickle.dump(lst,fp)
			print("Employee Data Saved as Record in File Sucessfully")
			print("-"*50)
			ch=input("Do u want to enter another employee details(yes/no):")
			if(ch.lower()=="no"):
				print("Thx for using this program")
				break
			print("-"*50)

#Main Program
saveempdata()

