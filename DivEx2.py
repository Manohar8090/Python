#Program for cal div of Two Numbers by accepting from Key Board
#DivEx2.py
try:
	print("Program Execution Started")
	a=input("\tEnter First Value:")
	b=input("\tEnter Second Value:")
	#convert 'a' 'b' into  floattype
	x=float(a)#--------exception generated Statement----ValueError
	y=float(b)  #--------exception generated Statement----ValueError
	z=x/y  #--------exception generated Statement----ZeroDivisionError
except ZeroDivisionError:
	print("\tDON'T ENTER ZERO FOR DEN...")
except ValueError:
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
else:
	print("-----------------else block---------------")
	print("\tFirst Value=",x)
	print("\tSecond Value=",y)
	print('\tDiv=',z)
finally:
	print("-----------------finally block---------------")
	print("Program Execution ended")


