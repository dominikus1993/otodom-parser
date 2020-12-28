import pandas as pd
import datetime
import streamlit as st
from typing import List
pd.set_option('display.max_colwidth', -1)
pd.set_option("display.max_rows", None, "display.max_columns", None)
def get_file_names():
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    dates: list[str] = pd.date_range(start="2020-12-10", end=today).to_native_types().tolist()
    return list(map(lambda d: f'otodom-{d}.csv', dates))


def load_csvs(filenames: List[str]):
    csvs = []
    for filename in filenames:
        try:
            df = pd.read_csv(f'./{filename}', index_col=None, header=0)
            csvs.append(df)
        except: 
            print("No file or dir")
    return pd.concat(csvs, axis=0, ignore_index=True)

def calc_avg_price_per_day(pd):
    return pd.groupby("Data", as_index=False)["Cena"].mean()

def calc_avg_price_per_meter_per_day(pd):
    return pd.groupby("Data", as_index=False)["Cena za m2"].mean()

def calc_avg_price_per_area(pd):
    return pd.groupby("Powierzchnia", as_index=False)["Cena"].mean()

def get_best_offers(data: pd.DataFrame):
    today = datetime.datetime.today().strftime("%d-%m-%Y")
    dt = data.query(f'Data == "{today}"').query("Powierzchnia > 40 & Powierzchnia < 60").query("Cena > 250000 & Cena < 400000")
    return dt[~dt["Dzielnica"].str.contains("Górna|Widzew|Śródmieście", na=False)].sort_values(by=['Cena'], ascending=False)

def get_flat_in_specyfic_district(data: pd.DataFrame, district: str):
    return data[data["Opis"].str.contains(f'{district}|{district.lower()}', na=False)]


data_load_state = st.text('Loading data...')

files = get_file_names()
df = load_csvs(files)
offers = get_best_offers(df)
avg_price_per_day = calc_avg_price_per_day(df)
avg_price_per_meter_per_day = calc_avg_price_per_meter_per_day(df)

data_load_state.text('Loading data...done!')

st.line_chart(avg_price_per_day.rename(columns={'Data':'index'}).set_index('index'));
st.line_chart(avg_price_per_meter_per_day.rename(columns={'Data':'index'}).set_index('index'));
st.write(offers[:15]["Link do ogłoszenia"])
st.write(get_flat_in_specyfic_district(offers, "Radogoszcz"))