#program for Reading the Data from Key Board and Write It to the File until we press @
#DynamicWriteEx1.py
with open("hyd.info","a") as fp:
    print("Enter the Information and Press @ to stop:")
    while(True):
        kbddata=input()
        if kbddata!="@":
            fp.write(kbddata+"\n")
        else:
            print("Data Written to the File--Verify")
            break

