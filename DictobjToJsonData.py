#Program for Converting Dict Object Data into JSON String data by using str()
#DictobjToJsonData.py
dictobj={'SNO': '100', 'NAME': 'Rossum', 'MARKS': '56.78'}
print("---------------------------------------------------------------------------")
print("Content of dict obj=",dictobj)
print("Type of dictobj=",type(dictobj))
print("---------------------------------------------------------------------------")
#Convert Dict Object data into  Json String data
jsonstrfmt=str(dictobj)
print("Content of Json String Format=",jsonstrfmt)
print("Type of jsonstrfmt=",type(jsonstrfmt))
print("---------------------------------------------------------------------------")
