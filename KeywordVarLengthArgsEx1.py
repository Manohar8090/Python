#program for showing the Need of Keyword Variable Length Arguments
#This Program will not execute at all bcoz PVM Performs Interpretation Process and Remembers Latest function Definition only.
#KeywordVarLengthArgsEx1.py
def disp(tno,tname,sub1,sub2):#Function Def-1
	print(tno,tname,sub1,sub2)

def disp(eno,ename,sal,cname,dsg): #Function Def-2
	print(eno,ename,sal,cname,dsg)

def disp(sno,sname,hb1,hb2,hb3,hb4): #Function Def-3
	print(sno,sname,hb1,hb2,hb3,hb4)


#main program
disp(tno=100,tname="KV",sub1="Python",sub2="Java") # Function Call-1 with 4 - Keyword args
disp(eno=200,ename="RS",sal=5.6,cname="TCS",dsg="SE") # Function Call-2 with 5 - Keyword args
disp(sno=300,sname="PR",hb1="eating",hb2="Sleeping",hb3="Chatting",hb4="Roaming")# Function Call-3 with 6 - Keyword args
