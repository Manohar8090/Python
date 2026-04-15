#program for Creating Only Date But Not Time
#DateEx1.py
from datetime import date as dt
td=dt.today()
print("Type of td=",type(td))
print("ToDay=",td)
print("\tYear=",td.year)
print("\tMonth=",td.month)
print("\tDay=",td.day)
