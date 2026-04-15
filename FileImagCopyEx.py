#program for Copying the content of one file into another File
#FileImagCopyEx.py
def imagefilecopy():
    try:
        with open("D:\\KVR-SUB\\kvr.png","rb") as rp:
            with open("E:\\KVR-python-11am\\Files\\NOTES\\pt.png","wb") as wp:
                srcfiledata=rp.read() # read data from source file
                wp.write(srcfiledata) # write source file data to dest file
                print("Image Copied Successfully")
    except FileNotFoundError:
        print("Source File Does not Exist")

#Main Program
imagefilecopy()