from typing import List
import datetime
import pandas as pd

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

def get_file_names():
    today = datetime.datetime.today()
    dates: list[str] = pd.date_range(start="2021-03-09", end=today).to_native_types().tolist()
    return list(map(lambda d: f'otodom-{d}.csv', dates))