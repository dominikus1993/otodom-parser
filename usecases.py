from datetime import date
import datetime
from services import Parser
from typing import List
from utils import generate_pages_urls
from model import Offer


class GetOffersUseCase:

    __offerParser: Parser

    def __init__(self, parser: Parser) -> None:
        self.offerParser = parser

    
    async def __load_offer(self, url: str, cityName: str) -> List[Offer]:
        
        return []

    async def load_offers(self, url: str, cityName: str, pages: int) -> List[Offer]: 
        pages_urls = generate_pages_urls(url, pages)
        return [Offer(1.2, ",", "", "", 12.12, 12.2, "", datetime.date(2008, 6, 24))];
