#Program for Reading the Data from CSV File by DictReader() in the form of dict
#CSVReadEx3.py
import csv
with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\product.csv","r") as fp:
    csvdr=csv.DictReader(fp) # here csvr is an object of <class, csv.DictReader>
    print("-------------------------------------------------")
    for record in csvdr: # here record is of type <class, dict>
        for k,v in record.items():
            print("\t{}-->{}".format(k,v))
        print("---------------------------")
    print("-------------------------------------------------")
