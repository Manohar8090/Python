#program for showing the Need of Keyword Variable Length Arguments
#PureKeywordVarLengthArgsEx2.py
def disp(**kvr): # here **kvr is called Key word Variable length arg and whose type is <class,dict>
	print("-"*50)
	if(len(kvr)==0):
		print("Does not Exit (K,v) Data:")
	else:
		for k,v in kvr.items():
			print("\t{}-->{}".format(k,v))
	print("-"*50)

#main program
disp(tno=100,tname="KV",sub1="Python",sub2="Java") # Function Call-1 with 4 - Keyword args
disp(eno=200,ename="RS",sal=5.6,cname="TCS",dsg="SE") # Function Call-2 with 5 - Keyword args
disp(sno=300,sname="PR",hb1="eating",hb2="Sleeping",hb3="Chatting",hb4="Roaming")# Function Call-3 with 6 - Keyword args
disp(cid=400,cname="DR")# Function Call-4 with 2- Keyword args
disp()