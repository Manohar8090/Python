#program for Finding Length of every word from List of words
#DictCompEx1.py
words=["Python","Java","DSA","Kotlin","C"]
wordslen={word:len(word)   for word in words} # Dict Comprehension
for k,v in wordslen.items():
	print("\t{}--->{}".format(k,v))
