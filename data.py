import datetime
import pandas as pd 
import math

def calc_avg_price_per_day(data)-> float:
    return data.groupby("Data", as_index=False)["Cena"].mean()

def calc_avg_price_per_meter_per_day(data):
    return data.groupby("Data", as_index=False)["Cena za m2"].mean()

def calc_avg_price_per_area(data):
    data["Area"] = data["Powierzchnia"].map(lambda x: math.ceil(float(x)))
    return data.query("Powierzchnia > 40 & Powierzchnia < 60").groupby("Area", as_index=False)["Cena"].mean()


def get_best_offers(data):
    today = datetime.date.today()
    dt = data.query(f'Data == "{today}"').query("Powierzchnia > 40 & Powierzchnia < 60").query("Cena > 250000 & Cena < 350000").drop_duplicates()
    return dt[~dt["Dzielnica"].str.contains("Górna|Widzew|Śródmieście", na=False)].sort_values(by=['Cena'], ascending=False)

def get_flat_in_specyfic_district(data: pd.DataFrame, district: str):
    return data[data["Opis"].str.contains(f'{district}|{district.lower()}', na=False)]