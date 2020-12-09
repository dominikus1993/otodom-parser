import pandas as pd
import datetime
from typing import List


def get_file_names():
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    dates: list[str] = pd.date_range(start="2020-12-08", end=today).to_native_types().tolist()
    return list(map(lambda d: f'otodom-{d}.csv', dates))


def load_csvs(filenames: List[str]):
    csvs = []
    for filename in filenames:
        df = pd.read_csv(f'./{filename}', index_col=None, header=0)
        csvs.append(df)
    return pd.concat(csvs, axis=0, ignore_index=True)


files = get_file_names()
data = load_csvs(files)

print(data)
