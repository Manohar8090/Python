#program for Finding Occurence(s) of each letter OR values in a Given Word
#FunLetterOccurencesEx.py
def getline():
    return input("Enter Line of Text:")

def getoccurences():
    word=getline()  # word="MISSISSIPPI"
    d={} # for placing value and its occurences
    for ch in word:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]=d.get(ch)+1
    else:
        print(d)
        print("length=",sum(d.values()))

#Main program
getoccurences()