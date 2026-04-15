#program for adding the new Records to the existing CSV File
#CSVAddRecordEx1.py
import csv
newrecord=[700,"Sunny Kumar",67.99] # record
with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\student.csv","a") as fp:
    csvwr=csv.writer(fp) # here csvwr is an object of <class, csv.writer>--step-5
    csvwr.writerow(newrecord)
    print("New record added to Existing CSV FileSuccessfully--verify")

