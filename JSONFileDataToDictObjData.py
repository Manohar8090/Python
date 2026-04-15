#program for Converting JSON File Data into Dict Object data by using load() of json  module
#JSONFileDataToDictObjData.py
import json
try:
	with open("E:\\KVR-PYTHON-11AM\\JSON\\NOTES\\student.json", "r") as fp:
		dictobj=json.load(fp)
		print("Content of dict obj=",dictobj)
		print("Type of dictobj=",type(dictobj))
		print("---------------------------------------------------------------------------")
		for k,v in dictobj.items():
			print("\t{}---->{}".format(k,v))
		print("---------------------------------------------------------------------------")
			

except FileNotFoundError:
	print("Json File Data Does not Exist")
