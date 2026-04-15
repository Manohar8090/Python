#Program for Converting DateTime to str datetime
#DatTimeToStrType.py
from datetime import datetime as dt
td=dt.now()
print("Todate={}  Type={}".format(td,type(td)))
std=dt.isoformat(td)
print("Todate={}  Type={}".format(std,type(std)))
