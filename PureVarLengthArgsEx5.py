#Program for Demonstrating the Need of  Variable Length Arguments
#PureVarLengthArgsEx5.py
def disp(sno,sname,*kvr,city="HYD"):  # here *kvr is called Variable Length args whose type is <class,tuple>
	print("-"*50)
	print("\tStudent  Number={}".format(sno))
	print("\tStudent  Name={}".format(sname))
	print("\tStudent  City={}".format(city))
	s=0
	for val in kvr:
		print("\t\t{}".format(val))
		s+=val
	print("\tSum={}".format(s))
	print("-"*50)


#main Program
disp(100,"RS",10,20,30,40,50)
disp(200,"TR",10,20,30,40) 
disp(300,"DR",10,20,30) 
disp(400,"SR",10,20) 
disp(500,"MC",10) 
disp(600,"SS")
#disp(700,"JH",city="MUM",1.2,2.3,3.4)--SyntaxError: positional argument follows keyword argument
disp(700,"JH",1.2,2.3,3.4,city="MUM")
disp(800,"KV",city="AP")