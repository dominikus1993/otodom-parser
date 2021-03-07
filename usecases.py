import datetime
from services import Parser, OffersStorage
from typing import List
from utils import generate_pages_urls
from model import Offer
from multiprocessing import Pool
import itertools
import logging

class GetOffersUseCase:

    __offerParser: Parser
    __storage: OffersStorage
    __logger: logging.Logger

    def __init__(self, parser: Parser, storage: OffersStorage, logger: logging.Logger) -> None:
        self.__offerParser = parser
        self.__storage = storage
        self.__logger = logger


    def load_offers(self, url: str, cityName: str, pages: int) -> List[Offer]: 
        pages_urls = generate_pages_urls(url, pages)
        with Pool(5) as p:
            self.__logger.info("Start parsing offers") 
            w = p.starmap_async(self.__offerParser.parse, map(lambda url: (url, cityName), pages_urls))
            w.wait() 
            offers = list(itertools.chain(*w.get()))
            self.__logger.info("Offers parsed")   
            return list(itertools.chain(*w.get()))
