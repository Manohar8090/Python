#This program denmonstrates How to Open the File
#FileOpenEx4.py
try:
    with open("hyd1.data") as fp:
        print("-----------------------------------------")
        print("\tFile Opened in Read Mode Sucessfully ")
        print("\tType of fp=",type(fp))
        print("\tIs File Closed=",fp.closed)
        print("\tFile Name=", fp.name)
        print("\tFile Opening Mode=",fp.mode)
        print("\tIs File Readable=",fp.readable())
        print("\tIs File Writable=",fp.writable())
        print("-----------------------------------------")
    print("I am out-off with open() as Indentation block")
    print("\tIs File Closed=", fp.closed)
except FileNotFoundError:
    print("File Does not Exist")
