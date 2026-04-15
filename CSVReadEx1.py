#Program for Reading the Data from CSV File by using _io.TextIOWrapper
#CSVReadEx1.py
with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\employee.csv","r") as fp:
    records=fp.read()
    print("----------------------------------------")
    print(records)
    print("----------------------------------------")