#program for Finding Max Length word from Given Line of Text
#FunMaxLengthWordEx.py
def getline():
    return input("Enter Line of Text:")

def getwordlength():
    line=getline() #Python is an Object Oriented Programming Lang
    if(len(line)==0):
        return {}  # returning empty dict
    elif(line.isspace()):
        return {} # returning empty dict
    else:
        words=line.split() #words=[Python,is,an,Object,Oriented,Programming, Lang]
        d={} # empty dict for storing word and Its length
        for word in words:
            d[word]=len(word)
        return d # # returning non-empty dict

def findmaxwordlength():
    d=getwordlength()
    if(len(d)==0):
        print("There is no data present in Dict and Can't Find Max length Word")
    else:
        lst=[]
        ml=max(d.values())
        for W,L in d.items():
            if(L==ml):
                lst.append(W)
        print("Max Length Word(s)")
        for val in lst:
            print(val)

#main Program
findmaxwordlength()