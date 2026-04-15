#Program for Converting JSON String Data into Dict Object by using json.loads()
#JsonStrdataTODictData.py
import json
jsonstrfmt='{"SNO":"100","NAME":"Rossum","MARKS":"56.78" }'
print("---------------------------------------------------------------------------")
print("Content of Json String Format=",jsonstrfmt)
print("Type of jsonstrfmt=",type(jsonstrfmt))
print("---------------------------------------------------------------------------")
#Convert json str data into dict object
dictobj=json.loads(jsonstrfmt)
print("Content of dict obj=",dictobj)
print("Type of dictobj=",type(dictobj))
print("---------------------------------------------------------------------------")
for k,v in dictobj.items():
	print("\t{}---->{}".format(k,v))
print("---------------------------------------------------------------------------")