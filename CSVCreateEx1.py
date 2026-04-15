#program for Creating the CSV File by using writer() of csv module
#CSVCreateEx1.py
import csv #Step-1
cols=["SNO","NAME","MARKS"] # Step-2
records=[[100,"Aniket",66.66],
       [200,"Rajesh",65.66],
       [300,"Rudra",77.77],
       [400,"KVR",11.11],
       [500,"Rishi",55.55] ] # Step-3
with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\student.csv","w") as fp: #Step-4
    csvwr=csv.writer(fp) # here csvwr is an object of <class, csv.writer>--step-5
    #here csvwr contains two fucntions 1) writerow() 2) writerows()
    csvwr.writerow(cols) # Step-6
    csvwr.writerows(records) #Step-7
    print("CSV File Created Successfully--verify")



