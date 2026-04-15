#Program for Obtaining List of -VE Values  from List of Values
#ContinueStmtEx6.py
lst=[10,-20,-30,40,50,-15,13,-24,56,0,-34]
nslist=[]
for val in lst:
    if(val>=0):
        continue
    nslist.append(val)
else:
    print("List of -VE Values")
    print(nslist)

# lst=[10, 20, 31, -33, -35, -37, 38, -42, 45, -46, 47]
# nslist=[]
# for val in lst:
#     if(val>=0):
#         continue
#     nslist.append(val)
# else:
#     print("List of -ve Values")
#     print(nslist)

# lst = [13, 15, 16, 18, -20, -22, 25]
# nslist = []
# for val in lst:
#     if(val<=0):
#         continue
#     nslist.append(val)
# else:
#     print("List of -ve Values")
#     print(nslist)