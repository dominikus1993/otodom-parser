from typing import Any, Callable, Iterable, List
import datetime
import pandas as pd
from typing import TypeVar
from itertools import groupby

def format_price(price: str) -> float:
    result = price.replace(",", ".").replace(" ", "")
    return float(result)

def get_csv_filename() -> str:
    today = datetime.date.today()
    return f'otodom-{today}.csv'

def get_district_name(district: str, city_name: str) -> str:
    return district.replace(f'Mieszkanie na sprzedaż: {city_name}, ', "")

def generate_pages_urls(url: str, maxPage: int) -> List[str]:
    return list(map(lambda page: f'{url}&page={page}',range(0, maxPage + 1)))

def load_csvs(paths: List[str]) -> Any:
    dtypes = { 'Opis': 'str', 'Dzielnica': 'str', 'Ilość pokoi': 'str', 'Cena': 'float', 'Powierzchnia': 'float', 'Cena za m2': 'float', 'Data': 'str', 'Link do ogłoszenia': 'str'}
    csvs = []
    for path in paths:
        try:
            df = pd.read_csv(path, index_col=None, header=0, dtype= dtypes)
            csvs.append(df)
        except:
            print("Error", path)

    return pd.concat(csvs, axis=0, ignore_index=True)

def get_file_names():
    today = datetime.datetime.today()
    dates: list[str] = pd.date_range(start="2021-03-09", end=today).astype(str).tolist()
    return list(map(lambda d: f'./data/otodom-{d}.csv', dates))


T = TypeVar('T');
def distinct_by(sequence: Iterable[T], func: Callable[[T], Any]) -> List[T]:
    return list([list(v)[0] for _, v in groupby(sequence, func)])
