import pandas as pd
import datetime

def datetimeRange(): 
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    return pd.date_range(start="2020-12-08",end=today).to_native_types().tolist()

#file = pd.read_csv("./otodom-09-12-2020.csv")

dates = datetimeRange()

print(dates)