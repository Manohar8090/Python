#program for Creating the CSV File by using DictWriter of csv module
#CSVCreateEx2.py
import csv #Step-1
cols=["PNO","PNAME","PRICE"] # Step-2
records=[ {"PNO":111,"PNAME":"KitKat","PRICE":20},
          {"PNO":222,"PNAME":"Cadburry with Silk with Nuts","PRICE":50},
          {"PNO":333,"PNAME":"ChacoPie","PRICE":30},
          {"PNO":444,"PNAME":"Bingo Lays","PRICE":20},
          {"PNO":555,"PNAME":"STRING","PRICE":40}]

with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\product.csv","w") as fp: #Step-4
    csvdwr=csv.DictWriter(fp,fieldnames=cols) # here csvdwr is an object of <class, csv.DictWriter>--step-5
    #here csvwr contains two fucntions 1) writeheader() 2) writerows()
    csvdwr.writeheader()  #Step-6
    csvdwr.writerows(records) #Step-7
    print("CSV File Created Successfully--verify")



