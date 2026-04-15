#Program for Demonstrating the Need of  Variable Length Arguments
#This Program will not execute at all bcoz PVM Performs Interpretation Process and Remembers Latest function Definition only.
#VarLengthArgsEx1.py
def disp(a,b,c,d,e): # Function Def-1
	print(a,b,c,d,e)
def disp(a,b,c,d): # Function Def-2
	print(a,b,c,d)
def disp(a,b,c): # Function Def-3
	print(a,b,c)
def disp(a,b): # Function Def-4
	print(a,b)
def disp(a): # Function Def-1
	print(a)

#main Program
disp(10,20,30,40,50) # Function Call-1 with 5-Pos Args
disp(10,20,30,40) # Function Call-2 with 4-Pos Args
disp(10,20,30) # Function Call-3 with 3-Pos Args
disp(10,20) # Function Call-4 with 2-Pos Args
disp(10) # Function Call-5 with 1-Pos Args