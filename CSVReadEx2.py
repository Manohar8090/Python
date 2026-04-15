#Program for Reading the Data from CSV File by reader() in the form list
#CSVReadEx2.py
import csv
with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\product.csv","r") as fp:
    csvr=csv.reader(fp) # here csvr is an object of <class, _csv.reader>
    print("-------------------------------------------------")
    for record in csvr: # here record is of type <class, list>
        for val in record:
            print("\t{}".format(val),end="\t")
        print()
    print("-------------------------------------------------")
