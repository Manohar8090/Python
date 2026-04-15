#Program for Demonstrating How to write the Data to the File
#FileWriteEx3.py
itrobj={1:"Python",2:"C",3:"DSA",4:"C++"}
with open("student2.data","a") as fp:
    fp.writelines(str(itrobj)+'\n')
    print("Data Written to the File")