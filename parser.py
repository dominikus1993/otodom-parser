import asyncio
from infrastructure import FakeParser

from usecases import GetOffersUseCase


a = asyncio.run(GetOffersUseCase(FakeParser()).load_offers("", "", 1))

print(a)