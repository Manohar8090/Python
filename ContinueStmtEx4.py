#ContinueStmtEx4.py
s="PYTHON"
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
print("-------------------------------------------")
#To Day My Req: I want to disp: PTHN
print("By using for Loop")
for ch in s: # s="PYTHON"
    if(ch in ["Y","O"]):
        continue
    print(ch,end="")
else:
    print()
    print("I am from else part of for loop")
print("-------------------------------------------")

# s="NUMPY"
# print("By using of for loop")
# for ch in s:
#     print("\t{}".format(ch))
# else:
#     print("I am from else part of the loop")
# print("-"*40)

# # To day my req: I want to disp: NUP

# print("By using of for loop")
# for ch in s: # NUMPY
#     if(ch in ["M","Y"]):
#         continue
#     print(ch,end="")
# else:
#     print()
#     print("I am from else part of the loop")
# print("-"*40)