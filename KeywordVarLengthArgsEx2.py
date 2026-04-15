#program for showing the Need of Keyword Variable Length Arguments
#This Program will  execute as it is.
#KeywordVarLengthArgsEx2.py
def disp(tno,tname,sub1,sub2):#Function Def-1
	print(tno,tname,sub1,sub2)
disp(tno=100,tname="KV",sub1="Python",sub2="Java") # Function Call-1 with 4 - Keyword args
#----------------------------------------------------------------------------------------------
def disp(eno,ename,sal,cname,dsg): #Function Def-2
	print(eno,ename,sal,cname,dsg)
disp(eno=200,ename="RS",sal=5.6,cname="TCS",dsg="SE") # Function Call-2 with 5 - Keyword args
#----------------------------------------------------------------------------------------------
def disp(sno,sname,hb1,hb2,hb3,hb4): #Function Def-3
	print(sno,sname,hb1,hb2,hb3,hb4)
disp(sno=300,sname="PR",hb1="eating",hb2="Sleeping",hb3="Chatting",hb4="Roaming")# Function Call-3 with 6 - Keyword args
