import datetime
from services import Parser
from typing import List
from utils import generate_pages_urls
from model import Offer
from multiprocessing import Pool
import itertools

class GetOffersUseCase:

    __offerParser: Parser

    def __init__(self, parser: Parser) -> None:
        self.__offerParser = parser


    def load_offers(self, url: str, cityName: str, pages: int) -> List[Offer]: 
        pages_urls = generate_pages_urls(url, pages)
        with Pool(5) as p:
            w = p.starmap_async(self.__offerParser.parse, map(lambda url: (url, cityName), pages_urls))
            w.wait()    
            return list(itertools.chain(*w.get()))
