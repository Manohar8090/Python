#Program for Creating Out Own str date with DateTime class
#DateDiffCalEx5.py
import datetime as dt
strdate1="2025-11-1"
strdate2="1/1/2025"
#Convert str date into datetime Object by using strptime()
d1=dt.datetime.strptime(strdate1,"%Y-%m-%d")
d2=dt.datetime.strptime(strdate2,"%d/%m/%Y")
diff=d1-d2
print("Diff between Two dates=",diff)
