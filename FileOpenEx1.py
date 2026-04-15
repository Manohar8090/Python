#This program denmonstrates How to Open the File
#FileOpenEx1.py
try:
    fp=open("hyd2.data")
except FileNotFoundError:
    print("File Does not Exist")
else:
    print("File Opened in Read Mode and we can perform read Operations")
    print("Type of fp=", type(fp))
finally:
    print("--------------------------------------")
    print("I am from finally Block")
    try:
        print("Still,Is File Closed=",fp.closed)
        print("-----------after close()---------------")
        fp.close()
        print("Still,Is File Closed=", fp.closed)
    except NameError:
        print("File Name itself not Opened-there No Question of Closing the file")
    finally:
        print("Thx for Choosing the files")


