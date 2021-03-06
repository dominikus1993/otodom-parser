import asyncio
from infrastructure import FakeParser

from usecases import GetOffersUseCase

OTODOM_URL = "https://www.otodom.pl/sprzedaz/mieszkanie/lodz/?search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004&search%5Border%5D=created_at_first%3Adesc"

a = GetOffersUseCase(FakeParser()).load_offers(OTODOM_URL, "Łódź", 10)

print(a)