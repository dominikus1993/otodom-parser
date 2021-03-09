from typing import List

def format_price(price: str) -> float:
    result = price.replace(",", ".").replace(" ", "")
    return float(result)

def get_district_name(district: str, city_name: str) -> str:
    return district.replace(f'Mieszkanie na sprzedaż: {city_name} ', "")

def generate_pages_urls(url: str, maxPage: int) -> List[str]:
    return list(map(lambda page: f'{url}&page={page}',range(0, maxPage + 1)))