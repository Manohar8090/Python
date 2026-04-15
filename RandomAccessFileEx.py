#Program for accessing Random Accessing the File Data
#RandomAccessFileEx.py
with open("E:\\KVR-PYTHON-11AM\\FILES\\hyd.info","rt") as fp:
	print("Initially, File Points to :",fp.tell()) # 0
	filedata=fp.read(3)
	print("File Data=",filedata) # HYD
	print("Now, Position of fp=",fp.tell())# 3
	filedata=fp.read(4)
	print("File Data=",filedata) #  _is_ 
	print("Now, Position of fp=",fp.tell())# 7
	filedata=fp.read(7)
	print("File Data=",filedata) # the cap
	print("Now, Position of fp=",fp.tell())# 14
	print("-------------------------------------------")
	filedata=fp.read()
	print("File Data=",filedata) # the cap
	print("Now, Position of fp=",fp.tell())# 
	print("-------------------------------------------")
	filedata=fp.read()
	print("File Data=",filedata) # the cap
	print("Now, Position of fp=",fp.tell())
	print("-------------------------------------------") # 225
	#Re-set the file pointer object to the Index 7
	fp.seek(7)
	print("Now, Position of fp=",fp.tell())
	filedata=fp.read(7)
	print("File Data=",filedata) # the cap
	print("Now, Position of fp=",fp.tell())# 14
	print("-------------------------------------------") 
	#Re-set the file pointer object to the Index 0
	fp.seek(0)
	print("Now, Position of fp=",fp.tell())# 0
	filedata=fp.read(10)
	print("File Data=",filedata) # 
	print("Now, Position of fp=",fp.tell())# 
