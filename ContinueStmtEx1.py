#ContinueStmtEx1.py
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
    if(ch=="T"):
        continue
    print(ch,end="")
else:
    print()
    print("I am from else part of for loop")
print("-------------------------------------------")

s="JAVASCRIPT"
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
print("-------------------------------------------")

# s="PYTHON"
# print("By using for Loop")
# for ch in s:
#     print("\t{}".format(ch))
# else:
#     print("I am from else part of the loop")
# print("------------------------------------")

# # To Day My Req: I want to dis: PYHON
# print("By using for loop")
# for ch in s: # PYTHON
#     if(ch=="T"):
#         continue
#     print(ch,end="")
# else:
#     print()
#     print("I am from else part of the loop")
# print("------------------------------------")

# s="NUMPY"
# print("By using the for loop")
# for ch in s:
#     print("\t{}".format(ch))
# else:
#     print("I am from the else part of the Loop")
# print("----------------------------------------")