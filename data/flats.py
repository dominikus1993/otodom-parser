import pandas as pd
import datetime
from typing import List


def get_file_names():
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    dates: list[str] = pd.date_range(start="2020-12-10", end=today).to_native_types().tolist()
    return list(map(lambda d: f'otodom-{d}.csv', dates))


def load_csvs(filenames: List[str]):
    csvs = []
    for filename in filenames:
        df = pd.read_csv(f'./{filename}', index_col=None, header=0)
        csvs.append(df)
    return pd.concat(csvs, axis=0, ignore_index=True)

def calc_avg_price_per_day(pd):
    return pd.groupby("Data", as_index=False)["Cena"].mean()


def calc_avg_price_per_area(pd):
    return pd.groupby("Powierzchnia", as_index=False)["Cena"].mean()

files = get_file_names()
df = load_csvs(files)
avg_price_per_day = calc_avg_price_per_day(df)
avg_price_per_area = calc_avg_price_per_area(df)
print(avg_price_per_day)
print(avg_price_per_area)