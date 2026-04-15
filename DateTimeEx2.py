#Program for Creating Date and Time abd Gets Misc Information
#DateTimeEx2.py
import datetime
td=datetime.datetime.now()
print("Type of td=",type(td))
print("Today date=",td)  
print("\tYear=",td.year)
print("\tMonth=",td.month)
print("\tDay=",td.day)
print("\tHour=",td.hour)
print("\tMinutes=",td.minute)
print("\tSeconds=",td.second)
print("\tMicro Seconds=",td.microsecond)
