#Program for cal div of Two Numbers by accepting from Key Board
#DivEx1.py
print("Program Execution Started")
a=input("Enter First Value:")
b=input("Enter Second Value:")
#convert 'a' 'b' into  floattype
x=float(a)#--------exception generated Statement----ValueError
y=float(b)  #--------exception generated Statement----ValueError
print("First Value=",x)
print("Second Value=",y)
z=x/y  #--------exception generated Statement----ZeroDivisionError
print('Div=',z)
print("Program Execution ended")
