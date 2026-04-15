#Program for Saving the Dict Object into the JSON File By using  dump() of json module
#DictObjToJsonFileData.py
import json
dictobj={'SNO': '100', 'NAME': 'Rossum', 'MARKS': '56.78'}
print("---------------------------------------------------------------------------")
print("Content of dict obj=",dictobj)
print("Type of dictobj=",type(dictobj))
print("---------------------------------------------------------------------------")
#save the dict data into the JSON File.
with open("E:\\KVR-PYTHON-11AM\\JSON\\NOTES\\student.json","w") as fp:
	json.dump(dictobj,fp)
	print("Dict data saved in json file as Dict Format--Verify")

