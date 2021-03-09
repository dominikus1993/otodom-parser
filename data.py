import pandas as pd

def calc_avg_price_per_day(data)-> float:
    return data.groupby("Data", as_index=False)["Cena"].mean()