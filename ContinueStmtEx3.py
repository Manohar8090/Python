#ContinueStmtEx3.py
s="PYTHON"
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("I am from else part of while loop")
print("-------------------------------------------")
#To Day My Req: I want to disp:PTHN
print("By using while Loop")
i=0
while(i<len(s)): # s="PYTHON"
    if(s[i]=="Y" or s[i]=="O"):
        i = i + 1
        continue
    print(s[i],end="")
    i=i+1
else:
    print()
    print("I am from else part of while loop")
print("-------------------------------------------")

# s="NUMPY"
# print("By using while loop")
# i=0
# while(i<len(s)):
#     print("\t{}".format(s[i]))
#     i=i+1
# else:
#     print("I am from else part of while loop")
# print("-"*40)

# #To Day my req: I wanr to disp: NMP
# print("By using of while loop")
# i=0
# while(i<len(s)): # s="PYTHON"
#     if(s[i]=="U" or s[i]=="Y"):
#         i= i+1
#         continue
#     print(s[i],end="")
#     i+=1
# else:
#     print()
#     print("I am from else part of while loop ")
# print("-"*40)