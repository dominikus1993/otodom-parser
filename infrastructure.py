

from model import Offer
from typing import List
from services import Parser

class FakeParser(Parser): 
    async def parse(self, url: str, city: str) -> List[Offer]:
        return []