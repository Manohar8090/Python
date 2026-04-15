#program for Finding Length of every word which contains Purely Alphabets from List of words
#DictCompEx2.py
words=["Python","1234","Java","456734","DSA","127989","Kotlin","C"]
wordslen={word:len(word)   for word in words  if word.isalpha() } # Dict Comprehension
for k,v in wordslen.items():
	print("\t{}--->{}".format(k,v))