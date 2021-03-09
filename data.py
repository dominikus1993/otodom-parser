import pandas as pd 


def calc_avg_price_per_day(data)-> float:
    return data.groupby("Data", as_index=False)["Cena"].mean()

def calc_avg_price_per_meter_per_day(data):
    return data.groupby("Data", as_index=False)["Cena za m2"].mean()

def calc_avg_price_per_area(data):
    return data.groupby("Powierzchnia", as_index=False)["Cena"].mean()
