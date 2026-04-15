#Program for Obtaining List of +VE Values  from List of Values
#ContinueStmtEx5.py
lst=[10,-20,-30,40,50,-15,13,-24,56,0,-34]
pslist=[]
for val in lst:
    if(val<=0):
        continue
    pslist.append(val)
else:
    print("List of +VE Values")
    print(pslist)

# lst=[10, 20, 30, -35, -45, 46, 49, -48, -57, 59]
# pslist=[]
# for val in lst:
#     if(val<=0):
#         continue
#     pslist.append(val)
# else:
#     print("List of +ve Values ")
#     print(pslist)