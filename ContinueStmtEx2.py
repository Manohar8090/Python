#ContinueStmtEx2.py
s="PYTHON"
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("I am from else part of while loop")
print("-------------------------------------------")
#To Day My Req: I want to disp: PYHON
print("By using while Loop")
i=0
while(i<len(s)): # s="PYTHON"
    if(s[i]=="T"):
        i = i + 1
        continue
      
    print(s[i],end="")
    i=i+1
else:
    print()
    print("I am from else part of while loop")
print("-------------------------------------------")

# s="PYTHON"
# print("By using of while loop")
# i=0
# while(i<len(s)):
#     print("\t{}".format(s[i]))
#     i+=1
# else:
#     print("I am from else part of the while loop")
# print("------------------------------------------")

# # To Day My Req: I want to disp: PYHON
# print("By using of While Loop")
# i=0
# while(i<len(s)): # s="PYTHON"
#     if(s[i]=="T"):
#         i+=1
#         continue
#     print(s[i], end="")
#     i+=1
# else:
#     print()
#     print("I am from else part of while loop")
# print("--------------------------------------")