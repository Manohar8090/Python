#This program denmonstrates How to Open the File
#FileOpenEx6.py
try:
    with open("E:\\KVR-PYTHON-11AM\\FILES\\notes\\hyd4.data","x+") as fp:
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
except FileExistsError:
    print("File already Exist-try with new File")