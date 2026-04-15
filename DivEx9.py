#Program for cal div of Two Numbers by accepting from Key Board--Most recommended to use
#DivEx9.py--Today 29/9/2025--KVR Programmer defined this code with Two exceptions
#This code will come for maintenance after 4 Years--2029---New Programmer--
try:
	print("Program Execution Started")
	a=input("\tEnter First Value:")
	b=input("\tEnter Second Value:")
	#convert 'a' 'b' into  floattype
	x=float(a)#--------exception generated Statement----ValueError
	y=float(b)  #--------exception generated Statement----ValueError
	z=x/y  #--------exception generated Statement----ZeroDivisionError
	s="PYTHON"
	ind=int(input("Enter Index within 0 to 5:"))
	print(s[ind])
except ZeroDivisionError:
	print("\tDON'T ENTER ZERO FOR DEN...")
except ValueError:
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
except Exception as z :
	print("\tOOOOOOOPS, Some Thing went Wrong!!! ",z)
else:
	print("-----------------else block---------------")
	print("\tFirst Value=",x)
	print("\tSecond Value=",y)
	print('\tDiv=',z)
finally:
	print("-----------------finally block---------------")
	print("Program Execution ended")


