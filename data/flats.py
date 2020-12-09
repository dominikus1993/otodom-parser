import pandas as pd
import datetime

def getCsvFiles(): 
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    dates = pd.date_range(start="2020-12-08",end=today).to_native_types().tolist()
    return list(map(lambda d: f'otodom-{d}.csv', dates))

#file = pd.read_csv("./otodom-09-12-2020.csv")

dates = datetimeRange()

print(dates)