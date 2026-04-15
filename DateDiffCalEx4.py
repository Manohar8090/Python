#Program for Creating Out Own date with DateTime class
#DateDiffCalEx4.py
import datetime as dt
d1=dt.datetime(2025,1,1,17,30,45)
d2=dt.datetime.now()
diff=d2-d1
print("Diff between two dates=",diff)
print("Type of diff var=",type(diff))
print("-------------------------------------------------")
