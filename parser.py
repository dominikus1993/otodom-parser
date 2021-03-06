import asyncio

from usecases import load_offers


a = asyncio.run(load_offers("", "", 1))

print(a)