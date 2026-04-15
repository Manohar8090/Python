#This program denmonstrates How to Open the File
#FileOpenEx5.py
try:
    with open("hyd2.data","w+") as fp:
        print("-----------------------------------------")
        print("\tFile Created amd Opened in write Mode Sucessfully ")
        print("\tType of fp=",type(fp))
        print("\tIs File Closed=",fp.closed)
        print("\tFile Name=", fp.name)
        print("\tFile Openg Mode=",fp.mode)
        print("\tIs File Readable=",fp.readable())
        print("\tIs File Writable=",fp.writable())
        print("-----------------------------------------")
    print("I am out-off with open() as Indentation block")
    print("\tIs File Closed=", fp.closed)
except FileNotFoundError:
    print("File Does not Exist")
