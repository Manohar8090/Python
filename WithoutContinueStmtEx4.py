#WithoutContinueStmtEx4.py
s="PYTHON"
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
print("-------------------------------------------")
#To Day My Req: I want to disp: PYHON
print("By using for Loop")
for ch in s: # s="PYTHON"
    if(ch=="T"):pass
    else:
        print(ch,end="")
else:
    print()
    print("I am from else part of for loop")
print("-------------------------------------------")