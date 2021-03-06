from datetime import date
import datetime
from typing import List
from model import Offer

async def load_offers(url: str, cityName: str, pages: int) -> List[Offer]: 
    return [Offer(1.2, ",", "", "", 12.12, 12.2, "", datetime.date(2008, 6, 24))];
