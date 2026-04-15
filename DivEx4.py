#Program for cal div of Two Numbers by accepting from Key Board
#DivEx4.py
try:
	print("Program Execution Started")
	a=input("\tEnter First Value:")
	b=input("\tEnter Second Value:")
	#convert 'a' 'b' into  floattype
	x=float(a)#--------exception generated Statement----ValueError
	y=float(b)  #--------exception generated Statement----ValueError
	z=x/y  #--------exception generated Statement----ZeroDivisionError
except ZeroDivisionError as z:
	print("\texception message..: ",z)
except ValueError as v:
	print("\texception message..: ",v)
else:
	print("-----------------else block---------------")
	print("\tFirst Value=",x)
	print("\tSecond Value=",y)
	print('\tDiv=',z)
finally:
	print("-----------------finally block---------------")
	print("Program Execution ended")


